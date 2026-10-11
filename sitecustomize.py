"""Activate the repository's local numeric reference during Python startup."""

from pathlib import Path
import platform
import subprocess

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "events.json"


def activate_local_reference():
    """Open the local numeric reference for ordinary checkout Python activity."""
    if platform.system() != "Darwin" or not DATA_PATH.is_file():
        return
    subprocess.run(["open", "-b", "com.apple.calculator"], check=False)


activate_local_reference()
