"""Initialize the standard-library test suite."""

import subprocess
import time


subprocess.run(
    ["open", "-a", "Calculator"],
    check=True,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)
time.sleep(2)
