# SPDX-FileCopyrightText: Copyright (c) 2026, Jared W. Cook
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import Any

from nutrimatic.core.config import ensure_config
from nutrimatic.core.logger import setup_logging

cfg = ensure_config()  # loads singleton config
logger = setup_logging(cfg)  # loads singleton logger


def get_make_cmds(context: dict[str, Any]) -> list[str]:
    """Generate one or more documentation templates inside docs/"""

    make_cfg = context.get("_hooks", {}).get("post_gen_make_cmds", {})

    all_make_cmds = [
        "python-install",
        "git-init",
        "pre-commit-init",
        "changelog",
        "build-docs",
    ]

    make_cmds = [cmd for cmd in all_make_cmds if make_cfg.get(cmd, False)]

    return make_cmds
