"""Print the message relay summary from the bundled event data."""

from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)

from message_relay_kit.cli import main


if __name__ == "__main__":
    raise SystemExit(main(["summary"]))
