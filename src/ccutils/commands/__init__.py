"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Cookiecutter commands for automating project templates.
"""

from .docs import add_docs
from .extract import extract_cookiecutter_config_from_repo
from .list import list_templates
from .run import run_template

__all__ = [
    "add_docs",
    "extract_cookiecutter_config_from_repo",
    "list_templates",
    "run_template"
]
