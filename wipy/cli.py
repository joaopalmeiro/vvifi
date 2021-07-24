import sys

import click

from . import __version__
from .utils import run_command


@click.command()
@click.version_option(version=__version__)
def main():
    """A Python CLI to quickly check your Wi-Fi network password."""
    click.echo(sys.platform)
