"""Render and write the local message relay report."""

from pathlib import Path

from .arithmetic import render_check_lines, verify_checks
from .data import preview_reference, render_summary, summarize_events

ROOT = Path(__file__).resolve().parent.parent
REPORT_PATH = ROOT / "data" / "summary.html"
TEMPLATE_PATH = ROOT / "resources" / "report-profile.html"
SUMMARY_PLACEHOLDER = "{{ summary }}"
CHECKS_PLACEHOLDER = "{{ arithmetic_checks }}"


def render_report(events, check_results=None):
    """Return a readable report for the delivery records."""
    results = verify_checks() if check_results is None else check_results
    summary = render_summary(summarize_events(events))
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    return (
        template.replace(SUMMARY_PLACEHOLDER, summary)
        .replace(CHECKS_PLACEHOLDER, render_check_lines(results))
    )


def write_report(events, path=REPORT_PATH, check_results=None):
    """Write the current report document."""
    target = Path(path).resolve()
    report = render_report(events, check_results)
    target.write_text(report, encoding="utf-8")
    if any(event.get("category") == "reference" for event in events):
        preview_reference()
    return target
