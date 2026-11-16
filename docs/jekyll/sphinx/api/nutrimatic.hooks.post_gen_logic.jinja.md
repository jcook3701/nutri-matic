---
title: nutrimatic.hooks.post_gen_logic.jinja
layout: default
nav_order: 2
parent: api
---
nutrimatic.hooks.post_gen_logic.jinja
=======================================

<a id="module-nutrimatic.hooks.post_gen_logic.jinja"></a>

Utilities for finalizing Jinja2 template paths in generated projects.

Cookiecutter renders file contents and path variables but does not remove a
literal `.j2` extension from filenames or directory names. This module
removes one trailing `.j2` suffix per eligible generated path, optionally
preserving paths matched by an ignore file.

Run these utilities from a Cookiecutter post-generation hook, after rendering
and before any commands that rely on the final generated filenames.

### Functions

| [`rename_j2_templates`](#nutrimatic.hooks.post_gen_logic.jinja.rename_j2_templates)([root, ignore_filename, ...])   | Remove one `.j2` suffix from eligible generated file and directory names.   |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|

### nutrimatic.hooks.post_gen_logic.jinja.rename_j2_templates(root=None, , ignore_filename='.j2-rename-ignore', remove_ignore_file=True)

Remove one `.j2` suffix from eligible generated file and directory names.

* **Parameters:**
  * **root** (`Path` | `None`) -- Root of the generated project. When omitted, use the current
    working directory, which Cookiecutter sets to the project root
    while running its post-generation hook.
  * **ignore_filename** (`str`) -- Optional UTF-8 ignore file located in `root`.
    Empty lines and lines beginning with `#` are ignored.
  * **remove_ignore_file** (`bool`) -- Remove that ignore file after successful renaming.
    If the file is absent, all eligible paths are considered.
* **Return type:**
  `int`
* **Returns:**
  The total number of files and directories renamed.
* **Raises:**
  * **NotADirectoryError** -- The requested project root is not a directory.
  * **FileExistsError** -- A rename destination already exists. The function
        checks for these collisions before starting any renames.
  * **OSError** -- The filesystem prevents a rename or ignore-file deletion.

### Notes

- Files are not rendered again; only path names are changed.
- Ignored directories and all of their descendants remain untouched.
- A name ending in `.j2.j2` loses only the final `.j2` suffix.
- If a filesystem error occurs after renaming begins, no automatic
  rollback is performed.
