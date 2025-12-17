"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from pathlib import Path

from nutrimatic.core.config import ensure_config
from nutrimatic.core.logger import setup_logging

cfg = ensure_config()  # loads singleton config
logger = setup_logging(cfg)  # loads singleton logger


def license_init(license_type: str) -> None:

    project_dir = Path.cwd()
    logger.info(f"{project_dir} {license_type}")

    # TODO: Remove NOTICE file if Apache-2.0 selected.
