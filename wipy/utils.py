import subprocess


def run_command(command: str) -> str:
    # More info: https://github.com/PyCQA/bandit#exclusions (`# nosec`)
    output, _ = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True
    ).communicate()

    return output.decode(encoding="utf-8")
