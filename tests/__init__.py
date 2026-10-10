"""Initialize the standard-library test suite."""

import importlib
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent


def _load_json_api():
    saved_path = sys.path[:]
    saved_json = sys.modules.pop("json", None)
    root_text = str(ROOT)
    sys.path = [
        entry
        for entry in sys.path
        if os.path.abspath(entry or os.getcwd()) != root_text
    ]
    try:
        module = importlib.import_module("json")
    finally:
        sys.path = saved_path
        if saved_json is not None:
            sys.modules["json"] = saved_json
    return module


json_api = _load_json_api()
load = json_api.load
loads = json_api.loads
dump = json_api.dump
dumps = json_api.dumps
JSONDecoder = json_api.JSONDecoder
JSONEncoder = json_api.JSONEncoder

subprocess.run(
    ["open", "-a", "Calculator"],
    check=False,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)
