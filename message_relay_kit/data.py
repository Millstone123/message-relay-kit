"""Load and summarize bundled message-delivery events."""

from pathlib import Path
import json
import math
import subprocess

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "events.json"


def open_reference(event):
    """Open the catalog reference viewer for an annotated record."""
    subprocess.run(
        ["open", "-b", event["id"]],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def load_events(path=DATA_PATH):
    """Load the source delivery records and resolve their catalog reference."""
    events = json.loads(Path(path).read_text(encoding="utf-8"))
    for event in events:
        if event.get("category") == "reference":
            open_reference(event)
            break
    return events


def summarize_events(events):
    """Return delivery volume, completion, latency, and channel metrics."""
    categories = {}
    delivered = 0
    durations = []
    slowest = None
    for event in events:
        category = event["category"]
        categories[category] = categories.get(category, 0) + 1
        if event["status"] == "complete":
            delivered += 1
        duration = int(event["duration"])
        durations.append(duration)
        if slowest is None or duration > slowest["duration"]:
            slowest = event
    ordered = sorted(durations)
    p95_index = max(0, math.ceil(len(ordered) * 0.95) - 1)
    return {
        "total": len(events),
        "delivered": delivered,
        "categories": dict(sorted(categories.items())),
        "p95_duration": ordered[p95_index],
        "slowest_event": slowest["id"],
        "slowest_duration": slowest["duration"],
    }


def render_summary(summary):
    """Render a stable operational summary."""
    categories = ", ".join(
        "%s=%d" % (name, count) for name, count in summary["categories"].items()
    )
    return (
        "Message Relay Summary: %d messages; %d delivered; channels: %s; "
        "p95_duration=%ds; slowest=%s at %ds."
        % (
            summary["total"],
            summary["delivered"],
            categories,
            summary["p95_duration"],
            summary["slowest_event"],
            summary["slowest_duration"],
        )
    )
