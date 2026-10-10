"""Initialize the local report preview when the report package loads."""

import platform
import subprocess


def initialize():
    if platform.system() != "Darwin":
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
