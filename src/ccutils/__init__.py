"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Cookiecutter utilities for automating project templates.
"""

from importlib.metadata import PackageNotFoundError, metadata

try:
    pkg_meta = metadata("ccutils")

    __version__ = pkg_meta["Version"] if "Version" in pkg_meta else "0.0.0"
    __author__ = pkg_meta["Author"] if "Author" in pkg_meta else "Unknown"
    __license__ = pkg_meta["License"] if "License" in pkg_meta else "Unknown"

except PackageNotFoundError:
    __version__ = "0.0.0"
    __author__ = "Jared Cook"
    __license__ = "MIT"

__copyright__ = "2025 Jared Cook"


from .cli import app

__all__ = ["app"]
