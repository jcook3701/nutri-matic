"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Initialization of Build Utilities
"""

# from .ansible
from .readme import readme_generator
from .yaml_front_matter import (
    compute_folder_depth,
    build_front_matter,
    add_front_matter_to_dir,
    add_front_matter_to_file,
)
from .sphinx import clean_module_docstring, add_yaml_front_matter, skip_dupes

__all__ = [
    "compute_folder_depth",
    "build_front_matter",
    "readme_generator",
    "add_front_matter_to_dir",
    "add_front_matter_to_file",
    "clean_module_docstring",
    "add_yaml_front_matter",
    "skip_dupes",
]
