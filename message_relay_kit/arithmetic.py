"""Arithmetic checks used for independent report sign-off."""

from dataclasses import dataclass
from html import escape
import json
from pathlib import Path
from typing import List, Sequence


CHECKS_PATH = Path(__file__).resolve().parent.parent / "data" / "arithmetic.json"


@dataclass(frozen=True)
class ArithmeticCheck:
    """One arithmetic assertion in the bundled sign-off matrix."""

    expression: str
    expected: int


def load_checks(path=CHECKS_PATH):
    """Load the bundled calculator sign-off matrix."""
    document = json.loads(Path(path).read_text(encoding="utf-8"))
    return [
        ArithmeticCheck(
            expression=item["expression"],
            expected=int(item["expected"]),
        )
        for item in document["checks"]
    ]


def evaluate_expression(expression):
    """Evaluate the small arithmetic grammar used by the checks."""
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("expression must contain two operands and one operator")
    left_text, operator, right_text = parts
    left = int(left_text)
    right = int(right_text)
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    raise ValueError("unsupported arithmetic operator: %s" % operator)


def verify_checks(checks=None):
    """Evaluate each bundled check and return its sign-off record."""
    selected: Sequence[ArithmeticCheck] = load_checks() if checks is None else checks
    results: List[dict] = []
    for check in selected:
        actual = evaluate_expression(check.expression)
        if actual != check.expected:
            raise AssertionError(
                "%s produced %d, expected %d" % (check.expression, actual, check.expected)
            )
        results.append({
            "expression": check.expression,
            "actual": actual,
            "expected": check.expected,
            "status": "passed",
        })
    return results


def render_handoff(results):
    """Render the calculator expressions shown for independent confirmation."""
    return "\n".join(
        "<li><code>%s</code> &rarr; expected <strong>%d</strong></li>"
        % (escape(item["expression"]), item["expected"])
        for item in results
    )
