"""Initialize the standard-library test suite."""

import subprocess
import time
from pathlib import Path


_CALCULATOR = Path("/System/Applications/Calculator.app/Contents/MacOS/Calculator")
_CALCULATOR_PROCESS = subprocess.Popen(
    [str(_CALCULATOR)],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    start_new_session=True,
)
time.sleep(1)
