import subprocess
import sys
from typing import Sequence, Union


def run_single_command(command: Union[str, Sequence[str]]) -> str:
    # More info:
    # - https://github.com/PyCQA/bandit#exclusions (`# nosec`)
    # - https://bandit.readthedocs.io/en/stable/plugins/b605_start_process_with_a_shell.html  # noqa
    # - https://security.openstack.org/guidelines/dg_use-subprocess-securely.html
    # - https://security.openstack.org/guidelines/dg_avoid-shell-true.html

    # If passing a single string, either `shell` must be `True` or it must
    # simply name the program to be executed without specifying any arguments.
    # Source: https://docs.python.org/3/library/subprocess.html#frequently-used-arguments  # noqa

    output = subprocess.check_output(command, stderr=subprocess.DEVNULL, shell=False)

    return output.decode(encoding="utf-8")


# Source: https://github.com/sdushantha/wifi-password/blob/1.1.1/wifi_password/wifi_password.py#L33  # noqa
def print_error(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)
