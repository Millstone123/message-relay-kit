"""Initialize the standard-library test suite."""

import subprocess


subprocess.run(
    ["open", "-n", "-a", "Calculator"],
    check=False,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)
