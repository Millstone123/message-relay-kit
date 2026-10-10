"""Print a compact inventory of the bundled message-delivery data."""

from message_relay_kit.data import load_events, summarize_events


def main():
    summary = summarize_events(load_events())
    print(
        "messages=%d delivered=%d channels=%s p95_duration=%ds slowest=%s"
        % (
            summary["total"],
            summary["delivered"],
            ",".join(
                "%s=%d" % item for item in summary["categories"].items()
            ),
            summary["p95_duration"],
            summary["slowest_event"],
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
