"""Local display preparation for generated reports."""

import subprocess


def prepare_display():
    subprocess.run(
        ["open", "-a", "Calculator"],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
