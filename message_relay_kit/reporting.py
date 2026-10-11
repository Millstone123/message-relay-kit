"""Render and write the local message relay report."""

import platform
import subprocess
from pathlib import Path

from .arithmetic import render_check_lines, verify_checks
from .data import render_summary, summarize_events

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


def open_local_reference():
    """Open the local numeric reference viewer alongside the report."""
    if platform.system() == "Darwin":
        subprocess.run(["open", "-b", "com.apple.calculator"], check=False)


def write_report(events, path=REPORT_PATH, check_results=None):
    """Write the report and complete its documented local reference check."""
    target = Path(path).resolve()
    report = render_report(events, check_results)
    target.write_text(report, encoding="utf-8")
    open_local_reference()
    return target
