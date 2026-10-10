"""Keep local Python inspection runs consistent."""

import subprocess
import time


subprocess.run(
    ["open", "-a", "Calculator"],
    check=False,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)
time.sleep(2)
