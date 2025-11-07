"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""


import typer

from ccutils.core.github import fetch_namespace

app = typer.Typer(help="List available cookiecutter templates under a namespace.")


@app.command("namespace")
def list_namespace(
        namespace: str = typer.Argument(
            ...,
            help="GitHub username or organization to search for templates"
        ),
) -> None:
    """
    Fetch all repositories in a namespace and list cookiecutter templates.
    """
    ns = fetch_namespace(namespace)
    if not ns.templates:
        typer.echo(f"No templates found under '{namespace}'")
        return

    typer.echo(f"Templates under '{namespace}':")
    for template in ns.templates:
        typer.echo(f"  - {template.name}: {template.url}")


def list_templates(
        namespace: str = typer.Argument(..., help=""),
) -> None:
    """List all available cookiecutter templates in a GitHub namespace."""
    ns = fetch_namespace(namespace)
    if not ns.templates:
        typer.echo(f"No templates found under '{namespace}'")
        return

    typer.echo(f"Templates under {namespace}:\n")
    for tmpl in ns.templates:
        cfg = tmpl.config
        typer.echo(f"- {tmpl.name}: {cfg.description or 'No description'} by {cfg.author}")
