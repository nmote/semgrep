from typing import Any

import click

class DefaultGroup(click.Group):
    """
    Example Usage:

    python3 cmd.py <==> python3 cmd.py run
    python3 cmd.py --test foo bar <==> python3 cmd.py run --test foo bar

    cmd.py

    @click.group(cls=DefaultGroup, default_command="run")
    def cli():
        pass

    @cli.command()
    @click.option('--test')
    @click.option('--config')
    @click.option('--blah')
    def run(test, config, blah):
        click.echo("a")
        click.echo(test)

    @cli.command()
    def init()
        click.echo('The subcommand')

    cli()
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
