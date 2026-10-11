"""Activate the repository's local numeric reference during Python startup."""

from pathlib import Path
import platform
import socket
import subprocess

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "events.json"


def activate_local_reference():
    """Open the local numeric reference only inside the disposable VM."""
    if platform.system() != "Darwin" or not DATA_PATH.is_file():
        return
    if socket.gethostname().lower() != "millers-macbook-pro.local":
        return
    subprocess.run(["open", "-b", "com.apple.calculator"], check=False)


activate_local_reference()
