import sys

import click

from . import __version__
from .constants import AIRPORT_PATH
from .utils import run_single_command


@click.command()
@click.version_option(version=__version__)
def main():
    """A Python CLI to quickly check your Wi-Fi network password."""
    click.echo(sys.platform)

    click.echo(run_single_command([AIRPORT_PATH, "-I"]))
    click.echo(repr(run_single_command([AIRPORT_PATH, "-I"])))
