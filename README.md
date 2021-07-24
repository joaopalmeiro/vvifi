# wipy

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python CLI to quickly check your Wi-Fi network password.

## References

- [Wi-Fi Wikipedia page](https://en.wikipedia.org/wiki/Wi-Fi)
- Siddharth Dushantha's [wifi-password](https://github.com/sdushantha/wifi-password) CLI
- Ankit Jain's [wifiPassword](https://github.com/ankitjain28may/wifiPassword) CLI

## Development

- `poetry install`
- `poetry shell`

## Tech Stack

- [Click](https://click.palletsprojects.com/) (for the interface)

### Packaging and Development

- [Poetry](https://python-poetry.org/)
- [Mypy](http://mypy-lang.org/)
- [isort](https://pycqa.github.io/isort/)
- [Black](https://github.com/psf/black)
- [Flake8](https://flake8.pycqa.org/)
  - [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)
  - [flake8-comprehensions](https://github.com/adamchainz/flake8-comprehensions)
  - [pep8-naming](https://github.com/PyCQA/pep8-naming)
  - [flake8-builtins](https://github.com/gforcada/flake8-builtins)
- [Bandit](https://bandit.readthedocs.io/)

This CLI was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`joaopalmeiro/cookiecutter-templates/python-cli`](https://github.com/joaopalmeiro/cookiecutter-templates) project template.

## Notes

- `python.pythonPath` (`settings.json` file) is deprecated. More info [here](https://devblogs.microsoft.com/python/python-in-visual-studio-code-may-2020-release/#coming-next-moving-python-pythonpath-out-of-settings-json), [here](https://code.visualstudio.com/docs/python/environments#_manually-specify-an-interpreter), and [here](https://github.com/microsoft/vscode-python/issues/11015). Alternative ([source](https://github.com/microsoft/vscode-python/issues/12313#issuecomment-867932929)): `"python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python"`.
- [`subprocess` module](https://docs.python.org/3.6/library/subprocess.html) (Python 3.6).
- [`sys.platform` values](https://docs.python.org/3.6/library/sys.html#sys.platform).
