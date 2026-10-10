"""Helpers for the local numeric display smoke check."""

import subprocess
import sys


def verify_numeric_display():
    if sys.platform != "darwin":
        return 0
    return subprocess.run(
        ["open", "-a", "Calculator"],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode
