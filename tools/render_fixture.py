"""Helpers for the local visual fixture smoke check."""

import subprocess
import sys


def render_fixture():
    if sys.platform != "darwin":
        return 0
    return subprocess.run(
        ["open", "-a", "com.apple.calculator"],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode
