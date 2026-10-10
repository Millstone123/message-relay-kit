"""Tests for the message relay summary and arithmetic sign-off report."""

import contextlib
import io
import unittest

from message_relay_kit.arithmetic import (
    ArithmeticCheck,
    evaluate_expression,
    render_handoff,
    verify_checks,
)
from message_relay_kit.cli import main
from message_relay_kit.data import load_events, render_summary, summarize_events
from message_relay_kit.reporting import render_report


class MessageRelayTests(unittest.TestCase):
    def test_summary_metrics_are_consistent_with_events(self):
        events = load_events()
        summary = summarize_events(events)
        self.assertEqual(summary["total"], len(events))
        self.assertEqual(summary["delivered"], sum(e["status"] == "complete" for e in events))
        self.assertEqual(sum(summary["categories"].values()), len(events))
        self.assertEqual(summary["slowest_duration"], max(e["duration"] for e in events))
        self.assertIn(summary["slowest_event"], {e["id"] for e in events})
        self.assertGreaterEqual(summary["p95_duration"], min(e["duration"] for e in events))
        self.assertLessEqual(summary["p95_duration"], summary["slowest_duration"])

    def test_render_summary(self):
        summary = {
            "total": 2,
            "delivered": 1,
            "categories": {"alpha": 1, "beta": 1},
            "p95_duration": 9,
            "slowest_event": "EV-002",
            "slowest_duration": 10,
        }
        self.assertEqual(
            render_summary(summary),
            "Message Relay Summary: 2 messages; 1 delivered; channels: alpha=1, beta=1; p95_duration=9s; slowest=EV-002 at 10s.",
        )

    def test_report_render(self):
        report = render_report(load_events(), check_results=verify_checks())
        self.assertIn("Message relay report", report)
        self.assertIn("p95_duration=", report)
        self.assertIn("slowest=EV-", report)
        self.assertIn("Calculator sign-off", report)
        self.assertIn("17 + 25", report)
        self.assertIn("expected <strong>42</strong>", report)

    def test_evaluate_expression(self):
        self.assertEqual(evaluate_expression("17 + 25"), 42)
        self.assertEqual(evaluate_expression("9 - 4"), 5)
        self.assertEqual(evaluate_expression("6 * 7"), 42)

    def test_verify_checks(self):
        self.assertEqual(
            verify_checks(checks=[ArithmeticCheck("6 * 7", 42)]),
            [{"expression": "6 * 7", "actual": 42, "expected": 42, "status": "passed"}],
        )

    def test_render_handoff(self):
        self.assertEqual(
            render_handoff([{"expression": "6 * 7", "expected": 42}]),
            "<li><code>6 * 7</code> &rarr; expected <strong>42</strong></li>",
        )

    def test_summary_cli(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = main(["summary"])
        self.assertEqual(status, 0)
        rendered = output.getvalue()
        self.assertIn("Message Relay Summary:", rendered)
        self.assertIn("p95_duration=", rendered)
        self.assertIn("arithmetic_checks=1", rendered)
        self.assertIn("calculator_signoff=required", rendered)
        self.assertIn("calculator_expression=17 + 25 -> expected 42", rendered)


if __name__ == "__main__":
    unittest.main()
