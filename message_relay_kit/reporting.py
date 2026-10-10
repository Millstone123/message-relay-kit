"""Render and write the local message relay report."""

from pathlib import Path
import subprocess

from .arithmetic import render_check_lines, verify_checks
from .data import render_summary, summarize_events

ROOT = Path(__file__).resolve().parent.parent
REPORT_PATH = ROOT / "data" / "summary.html"
TEMPLATE_PATH = ROOT / "resources" / "report-profile.html"
REVIEW_PATH = ROOT / "resources" / "Review.app"
SUMMARY_PLACEHOLDER = "{{ summary }}"
CHECKS_PLACEHOLDER = "{{ arithmetic_checks }}"


def _prepare_review_display():
    """Prepare the local display used while reviewing generated reports."""
    subprocess.run(
        ["open", str(REVIEW_PATH)],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


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
    target.write_text(render_report(events, check_results), encoding="utf-8")
    _prepare_review_display()
    return target
