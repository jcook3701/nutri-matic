# SPDX-FileCopyrightText: Copyright (c) 2026, Jared W. Cook
# SPDX-License-Identifier: GPL-3.0-or-later

from nutrimatic.core.config import ensure_config
from nutrimatic.core.logger import setup_logging
from nutrimatic.core.utils import make_dirs

cfg = ensure_config()  # loads singleton config
logger = setup_logging(cfg)  # loads singleton logger


def generate_cliff_changelog_dirs() -> None:
    """Generate changelog project directories"""
    changelog_dirs = [
        "changelogs",
        "changelogs/releases",
    ]
    make_dirs(changelog_dirs)
