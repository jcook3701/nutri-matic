"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from ccutils.core import models
from ccutils.core.models import *

from .config import ensure_config
from .github import fetch_namespace

# Merge __all__ dynamically
__all__ = list(getattr(models, "__all__", [name for name in dir(models) if not name.startswith("_")]))
__all__ += ["ensure_config", "fetch_namespace"]
