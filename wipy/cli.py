import sys

import click
from string_utils import strip_margin

from . import __version__
from .constants import AIRPORT_PATH, DEVICE_RE, NETWORK_SYMBOL, SSID_RE
from .utils import print_error, run_single_command


# Typing: https://github.com/pallets/click/blob/8.0.0/src/click/decorators.py#L356
def print_networks(ctx: click.Context, param: click.Parameter, value: bool) -> None:
    if not value or ctx.resilient_parsing:
        return

    hardware = run_single_command(["networksetup", "-listallhardwareports"]).strip()

    device = DEVICE_RE.search(hardware)

    if device:
        networks = run_single_command(
            [
                "networksetup",
                "-listpreferredwirelessnetworks",
                device.group("device"),
            ]
        ).rstrip()

        click.echo(networks)
        # click.echo(repr(networks))

    ctx.exit()


@click.command()
# More info:
# - https://click.palletsprojects.com/en/7.x/options/#boolean-flags
# - https://click.palletsprojects.com/en/7.x/options/#callbacks-and-eager-options
@click.option(
    "--networks",
    is_flag=True,
    callback=print_networks,
    expose_value=False,
    is_eager=True,
    help="Show the names of saved Wi-Fi networks and exit.",
)
@click.version_option(version=__version__)
@click.pass_context
def main(ctx: click.Context):
    """A Python CLI to quickly check your Wi-Fi network password."""
    if sys.platform.startswith("darwin"):
        # macOS.
        wifi_info = run_single_command([AIRPORT_PATH, "-I"])
        wifi_info = strip_margin(wifi_info).rstrip()

        # click.echo(repr(wifi_info))
        # click.echo(wifi_info)

        ssid = SSID_RE.search(wifi_info)

        # click.echo(repr(ssid))
        # click.echo(ssid)

        # More info:
        # - https://github.com/sdushantha/wifi-password/blob/1.1.1/wifi_password/wifi_password.py#L78  # noqa
        # - https://apple.stackexchange.com/questions/176119/how-to-access-the-wi-fi-password-through-terminal  # noqa
        if ssid:
            name = ssid.group("name")

            password = run_single_command(
                [
                    "security",
                    "find-generic-password",
                    "-l",  # or `-a`
                    name,
                    "-D",
                    "AirPort network password",
                    "-w",
                ]
            ).rstrip()

            click.secho(f"{NETWORK_SYMBOL} {name}\n", bold=True)
            click.echo(password)
    else:
        print_error(f"{repr(sys.platform)} is not supported.", ctx)
