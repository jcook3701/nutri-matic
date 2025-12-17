"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from .ansible import generate_ansible_dirs
from .auto_vars import replace_placeholders_in_dir
from .changelogs import generate_cliff_changelog_dirs
from .docs import generate_docs_templates
from .utils import make_dirs

__all__ = [
    "generate_ansible_dirs",
    "generate_cliff_changelog_dirs",
    "generate_docs_templates",
    "make_dirs",
    "replace_placeholders_in_dir",
]
