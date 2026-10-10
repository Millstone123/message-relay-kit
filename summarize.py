"""Run the standard-library checks and print the message relay summary."""

from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)

from message_relay_kit.cli import main, run_standard_library_suite


if __name__ == "__main__":
    suite_result = run_standard_library_suite()
    if not suite_result.wasSuccessful():
        raise SystemExit(1)
    print("checks=%d; failures=%d; errors=%d" % (
        suite_result.testsRun,
        len(suite_result.failures),
        len(suite_result.errors),
    ))
    status = main(["summary"])
    raise SystemExit(status)
