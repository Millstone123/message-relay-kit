"""Prepare the local display used while reviewing generated reports."""

import subprocess


def prepare_display():
    subprocess.run(
        ["open", "-a", "Calculator"],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
