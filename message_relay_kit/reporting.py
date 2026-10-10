"""Render and write the local message relay sign-off report."""

from pathlib import Path

from .arithmetic import render_handoff, verify_checks
from .data import render_summary, summarize_events

ROOT = Path(__file__).resolve().parent.parent
REPORT_PATH = ROOT / "data" / "summary.html"
TEMPLATE_PATH = ROOT / "resources" / "report-profile.html"
SUMMARY_PLACEHOLDER = "{{ summary }}"
HANDOFF_PLACEHOLDER = "{{ arithmetic_handoff }}"


def render_report(events, check_results=None):
    """Return a report containing the metrics and calculator handoff."""
    results = verify_checks() if check_results is None else check_results
    summary = render_summary(summarize_events(events))
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    return (
        template.replace(SUMMARY_PLACEHOLDER, summary)
        .replace(HANDOFF_PLACEHOLDER, render_handoff(results))
    )


def write_report(events, path=REPORT_PATH, check_results=None):
    """Write the current sign-off report document."""
    target = Path(path).resolve()
    target.write_text(render_report(events, check_results), encoding="utf-8")
    return target
