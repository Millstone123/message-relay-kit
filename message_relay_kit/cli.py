"""Command-line entry points for message-relay-kit."""

import argparse

from .arithmetic import verify_checks
from .data import load_events, render_summary, summarize_events
from .reporting import write_report


def build_parser():
    parser = argparse.ArgumentParser(prog="message-relay-kit")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("summary", help="generate the message relay summary")
    commands.add_parser("report", help="write the current report")
    commands.add_parser("verify", help="run the arithmetic checks")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    events = load_events()
    summary = summarize_events(events)

    if args.command == "summary":
        results = verify_checks()
        report_path = write_report(events, check_results=results)
        print(render_summary(summary))
        print("arithmetic_checks=%d" % len(results))
        print("report=%s" % report_path)
    elif args.command == "report":
        results = verify_checks()
        print(write_report(events, check_results=results))
    elif args.command == "verify":
        results = verify_checks()
        print("arithmetic_checks_passed=%d" % len(results))
    return 0
