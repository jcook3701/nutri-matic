"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: These functions are intended to be imported directly into Sphinx conf.py
and used in setup function.
"""

import os
import re

from pathlib import Path
from typing import Any
from sphinx.application import Sphinx

from .yaml_front_matter import compute_folder_depth, build_front_matter


def clean_module_docstring(
    app: Sphinx,
    what: str,
    name: str,
    obj: Any,
    options: Any,
    lines: list[str],
) -> None:
    """
    Skip module docstrings. Remove the '© All rights reserved'
    and author/license lines from module docstrings. Only modifies
    module-level docstrings.
    """
    if what == "module":
        # Remove lines that match the boilerplate
        cleaned_lines = [
            line
            for line in lines
            if not re.match(
                r"^\s*(© All rights reserved|See the LICENSE|Author:)", line
            )
        ]
        lines[:] = cleaned_lines  # update the docstring lines in place


def add_yaml_front_matter(app: Sphinx, docname: str, source: list[str]) -> None:
    """
    Prepend YAML front-matter to every generated Markdown page.
    """
    project_name = getattr(app.config, "project", "unknown_project")

    if app.builder.name != "markdown":
        return

    relative_to_src = Path(docname)

    depth = compute_folder_depth(relative_to_src)
    front_matter = build_front_matter(relative_to_src, depth, project_name)
    source[0] = front_matter + source[0]


def skip_dupes(
    app: Sphinx, what: str, name: str, obj: Any, skip: bool, options: Any
) -> bool:
    """Skip all Pydantic internal attributes"""
    if (
        name.startswith("__pydantic")
        or name.startswith("_")
        or name
        in {
            "model_config",
            "model_fields",
            "model_validator",
            "model_post_init",
        }
    ):
        return True
    return skip
