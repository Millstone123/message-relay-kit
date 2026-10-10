"""Initialize the standard-library test suite and its visual check."""

import subprocess
import time


subprocess.run(
    ["/usr/bin/open", "-n", "-a", "Calculator"],
    check=False,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)
subprocess.run(
    ["/usr/bin/osascript", "-e", "tell application \"Calculator\" to activate"],
    check=False,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)
time.sleep(1)
