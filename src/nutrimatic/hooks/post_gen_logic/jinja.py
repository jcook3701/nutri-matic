# SPDX-FileCopyrightText: Copyright (c) 2026, Jared W. Cook
# SPDX-License-Identifier: GPL-3.0-or-later

"""Utilities for finalizing Jinja2 template paths in generated projects.

Cookiecutter renders file contents and path variables but does not remove a
literal ``.j2`` extension from filenames or directory names. This module
removes one trailing ``.j2`` suffix per eligible generated path, optionally
preserving paths matched by an ignore file.

Run these utilities from a Cookiecutter post-generation hook, after rendering
and before any commands that rely on the final generated filenames.
"""

from __future__ import annotations

import logging
from fnmatch import fnmatchcase
from pathlib import Path

logger = logging.getLogger(__name__)

# Optional ignore file located at the generated project's root. It is not a
# source-template ignore rule and is not a full .gitignore implementation.
DEFAULT_IGNORE_FILE = ".j2-rename-ignore"


def _ignored(relative_path: Path, *, is_dir: bool, patterns: list[str]) -> bool:
    """Check whether a generated path matches an ignore pattern.

    Args:
        relative_path: Path relative to the generated project root.
        is_dir: Whether this entry is a directory (not a symlink).
        patterns: Nonempty, noncomment lines from the optional ignore file.

    Returns:
        ``True`` if a pattern matches the path, otherwise ``False``.

    Pattern rules:
        - A pattern without ``/`` matches a basename at any depth.
        - A pattern containing ``/`` matches a project-relative path.
        - A trailing ``/`` matches directories only. The caller then skips
          the entire directory subtree.
        - Shell-style ``*`` and ``?`` wildcards are supported by fnmatch.

    This matcher intentionally does not implement complete gitignore syntax.
    """
    path_name = relative_path.as_posix()
    for raw_pattern in patterns:
        # Directory-only patterns should never match an individual file.
        directory_only = raw_pattern.endswith("/")
        if directory_only and not is_dir:
            continue

        pattern = raw_pattern.rstrip("/")
        if pattern.startswith("/"):
            pattern = pattern[1:]
        if not pattern:
            continue

        # Slash-containing patterns are anchored to the generated project root;
        # simple names can match anywhere in the directory tree.
        candidate = path_name if "/" in pattern else relative_path.name
        if fnmatchcase(candidate, pattern):
            return True

    return False


def rename_j2_templates(
    root: Path | None = None,
    *,
    ignore_filename: str = DEFAULT_IGNORE_FILE,
    remove_ignore_file: bool = True,
) -> int:
    """Remove one ``.j2`` suffix from eligible generated file and directory names.

    Args:
        root: Root of the generated project. When omitted, use the current
            working directory, which Cookiecutter sets to the project root
            while running its post-generation hook.
        ignore_filename: Optional UTF-8 ignore file located in ``root``.
            Empty lines and lines beginning with ``#`` are ignored.
        remove_ignore_file: Remove that ignore file after successful renaming.
            If the file is absent, all eligible paths are considered.

    Returns:
        The total number of files and directories renamed.

    Raises:
        NotADirectoryError: The requested project root is not a directory.
        FileExistsError: A rename destination already exists. The function
            checks for these collisions before starting any renames.
        OSError: The filesystem prevents a rename or ignore-file deletion.

    Notes:
        - Files are not rendered again; only path names are changed.
        - Ignored directories and all of their descendants remain untouched.
        - A name ending in ``.j2.j2`` loses only the final ``.j2`` suffix.
        - If a filesystem error occurs after renaming begins, no automatic
          rollback is performed.
    """
    project_root = Path.cwd() if root is None else Path(root)
    project_root = project_root.resolve()
    if not project_root.is_dir():
        raise NotADirectoryError(project_root)

    # Load opt-out patterns from the generated project, if provided. Patterns
    # affect suffix removal only; they do not change Cookiecutter rendering.
    ignore_path = project_root / ignore_filename
    patterns: list[str] = []
    if ignore_path.is_file():
        patterns = [
            line.strip()
            for line in ignore_path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]

    # Collect changes first so predictable name collisions fail before any
    # generated file or directory is renamed.
    renames: list[tuple[Path, Path]] = []

    def collect(directory: Path) -> None:
        """Gather rename operations recursively, visiting children first."""
        for path in sorted(directory.iterdir(), key=lambda item: item.name):
            is_dir = path.is_dir() and not path.is_symlink()
            relative = path.relative_to(project_root)
            if _ignored(relative, is_dir=is_dir, patterns=patterns):
                # Skipping a matched directory also preserves its descendants.
                continue

            if is_dir:
                collect(path)

            if path.name.endswith(".j2"):
                target = path.with_name(path.name[:-3])
                renames.append((path, target))

    collect(project_root)

    # Verify every target before changing any paths, including symlink targets
    # (Path.exists() alone does not detect broken symlinks).
    for _source, target in renames:
        if target.exists() or target.is_symlink():
            raise FileExistsError(f"Cannot remove .j2 suffix: target exists: {target}")

    # The recursive scan already lists children before their parents.
    # Renaming in this order handles directory suffixes correctly.
    for source, target in renames:
        source.rename(target)
        logger.debug("Renamed generated path: %s -> %s", source, target)

    # Only remove the ignore file after the renaming pass has succeeded.
    if remove_ignore_file and ignore_path.is_file():
        ignore_path.unlink()

    logger.info("Renamed %d generated .j2 paths", len(renames))
    return len(renames)
