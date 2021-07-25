import sys

import click
from string_utils import strip_margin

from . import __version__
from .constants import AIRPORT_PATH, NETWORK_SYMBOL, SSID_RE
from .utils import print_error, run_single_command


@click.command()
@click.version_option(version=__version__)
def main():
    """A Python CLI to quickly check your Wi-Fi network password."""
    if sys.platform.startswith("darwin"):
        # macOS.
        wifi_info = run_single_command([AIRPORT_PATH, "-I"])
        wifi_info = strip_margin(wifi_info).rstrip()

        # click.echo(repr(wifi_info))
        # click.echo(wifi_info)

        ssid = SSID_RE.search(wifi_info).group("name")

        # click.echo(repr(ssid))
        # click.echo(ssid)

        # More info:
        # - https://github.com/sdushantha/wifi-password/blob/1.1.1/wifi_password/wifi_password.py#L78  # noqa
        # - https://apple.stackexchange.com/questions/176119/how-to-access-the-wi-fi-password-through-terminal  # noqa
        password = run_single_command(
            [
                "security",
                "find-generic-password",
                "-l",  # or `-a`
                ssid,
                "-D",
                "AirPort network password",
                "-w",
            ]
        ).rstrip()

        click.secho(f"{NETWORK_SYMBOL} {ssid}\n", bold=True)
        click.echo(password)
    else:
        print_error(f"{repr(sys.platform)} is not supported.")
