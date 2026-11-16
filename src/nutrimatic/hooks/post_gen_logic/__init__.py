# SPDX-FileCopyrightText: Copyright (c) 2026, Jared W. Cook
# SPDX-License-Identifier: GPL-3.0-or-later

"""Public post-generation helpers shared across Nutri-Matic Cookiecutter projects.

These imports expose project initialization, documentation generation, and
Jinja2 suffix cleanup from one stable package entry point.
"""

from .ansible import generate_ansible_dirs
from .auto_vars import replace_placeholders_in_dir
from .changelogs import generate_cliff_changelog_dirs
from .docs import generate_docs_templates
from .jinja import rename_j2_templates
from .make import get_make_cmds

__all__ = [
    "generate_ansible_dirs",
    "generate_cliff_changelog_dirs",
    "generate_docs_templates",
    "get_make_cmds",
    "rename_j2_templates",
    "replace_placeholders_in_dir",
]
