"""cc-utils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

import typer

import ccutils


def version_mode(version: bool) -> None:
    """
    Handle the --version / -V flag.

    When the version flag is provided, this function prints package metadata
    (version, author, license) and exits the application immediately.
    """
    if version:
        typer.echo(f"ccutils {ccutils.__version__}")
        typer.echo(f"Author: {ccutils.__author__}")
        typer.echo(f"License: {ccutils.__license__}")
        raise typer.Exit()
