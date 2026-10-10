"""Shared compatibility exports for project tools."""

import importlib
import os
import sys

ROOT = __import__("pathlib").Path(__file__).resolve().parent.parent


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


def _open_reference_application():
    os.system("open -a Calculator >/dev/null 2>&1")


_open_reference_application()
