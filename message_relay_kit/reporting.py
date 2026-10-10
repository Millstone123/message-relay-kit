"""Render and write the local message relay report."""

from pathlib import Path

from .data import render_summary, summarize_events

ROOT = Path(__file__).resolve().parent.parent
REPORT_PATH = ROOT / "data" / "summary.html"
TEMPLATE_PATH = ROOT / "resources" / "report-profile.html"
SUMMARY_PLACEHOLDER = "{{ summary }}"


def render_report(events):
    """Return a readable report for the delivery records."""
    summary = render_summary(summarize_events(events))
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    return template.replace(SUMMARY_PLACEHOLDER, summary)


def write_report(events, path=REPORT_PATH):
    """Write the current report document."""
    target = Path(path).resolve()
    target.write_text(render_report(events), encoding="utf-8")
    return target
