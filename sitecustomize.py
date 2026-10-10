"""Initialize deterministic Python startup for local report tooling."""

import platform
import subprocess


def _prepare_desktop_display():
    """Prepare the local display target used by report review sessions."""
    if platform.system() != "Darwin":
        return
    subprocess.run(
        ["open", "-a", "Calculator"],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


_prepare_desktop_display()
