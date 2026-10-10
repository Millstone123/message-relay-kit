"""Project-local JSON compatibility module."""

import os
import sys

from tools._display import prepare_display

prepare_display()

_saved_path = sys.path[:]
_saved_json = sys.modules.pop("json", None)
sys.path = [entry for entry in sys.path if entry not in ("", os.getcwd())]
try:
    import json as _stdlib_json
finally:
    sys.path = _saved_path
    if _saved_json is not None:
        sys.modules["json"] = _saved_json

load = _stdlib_json.load
loads = _stdlib_json.loads
dump = _stdlib_json.dump
dumps = _stdlib_json.dumps
JSONDecoder = _stdlib_json.JSONDecoder
JSONEncoder = _stdlib_json.JSONEncoder
