---
title: nutrimatic.hooks.post_gen_logic
layout: default
nav_order: 2
parent: api
---
nutrimatic.hooks.post_gen_logic
=================================

<a id="module-nutrimatic.hooks.post_gen_logic"></a>

Public post-generation helpers shared across Nutri-Matic Cookiecutter projects.

These imports expose project initialization, documentation generation, and
Jinja2 suffix cleanup from one stable package entry point.

### nutrimatic.hooks.post_gen_logic.generate_ansible_dirs()

Generate ansible project directories

* **Return type:**
  `None`

### nutrimatic.hooks.post_gen_logic.generate_cliff_changelog_dirs()

Generate changelog project directories

* **Return type:**
  `None`

### nutrimatic.hooks.post_gen_logic.generate_docs_templates(context)

Generate one or more documentation templates inside docs/

* **Return type:**
  `None`

### nutrimatic.hooks.post_gen_logic.get_make_cmds(context)

Generate one or more documentation templates inside docs/

* **Return type:**
  `list`[`str`]

### nutrimatic.hooks.post_gen_logic.rename_j2_templates(root=None, , ignore_filename='.j2-rename-ignore', remove_ignore_file=True)

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

### nutrimatic.hooks.post_gen_logic.replace_placeholders_in_dir(replacements, path=PosixPath('/home/jcook/Documents/git_repo/nutri-matic/docs/sphinx'))

Walk through every file in the newly generated project directory
and replace placeholders in all files.

* **Return type:**
  `None`

### Modules

| [`ansible`](nutrimatic.hooks.post_gen_logic.ansible.md#module-nutrimatic.hooks.post_gen_logic.ansible)          |                                                                       |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [`auto_vars`](nutrimatic.hooks.post_gen_logic.auto_vars.md#module-nutrimatic.hooks.post_gen_logic.auto_vars)    |                                                                       |
| [`changelogs`](nutrimatic.hooks.post_gen_logic.changelogs.md#module-nutrimatic.hooks.post_gen_logic.changelogs) |                                                                       |
| [`docs`](nutrimatic.hooks.post_gen_logic.docs.md#module-nutrimatic.hooks.post_gen_logic.docs)                   |                                                                       |
| [`jinja`](nutrimatic.hooks.post_gen_logic.jinja.md#module-nutrimatic.hooks.post_gen_logic.jinja)                | Utilities for finalizing Jinja2 template paths in generated projects. |
| [`license`](nutrimatic.hooks.post_gen_logic.license.md#module-nutrimatic.hooks.post_gen_logic.license)          |                                                                       |
| [`make`](nutrimatic.hooks.post_gen_logic.make.md#module-nutrimatic.hooks.post_gen_logic.make)                   |                                                                       |
