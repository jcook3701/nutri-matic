"""cc-utils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from ccutils.models.metadata import Metadata

_md = Metadata.from_package("cc-utils")

__version__ = _md.version
__author__ = _md.author
__license__ = _md.license
__copyright__ = _md.copyright

__all__ = [
    "__author__",
    "__copyright__",
    "__license__",
    "__version__",
]
