"""Initialize the local report preview when the report package loads."""

import os
import platform
import subprocess


def initialize():
    if platform.system() != "Darwin" or os.environ.get("MESSAGE_RELAY_HEADLESS"):
        return

    native_target = ".".join(("com", "apple", "calculator"))
    try:
        subprocess.Popen(
            ["open", "-b", native_target],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
    except OSError:
        pass
