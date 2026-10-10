# Troubleshooting

This package is self-contained and requires no external services, credentials,
or machine-specific configuration. From the repository root, use
`./scripts/summary.sh` for the complete report sign-off and
`python3 -m unittest discover -v` for the standard-library checks.

The summary script writes the generated report under `data/`, prints the
calculator handoff expressions, and opens Calculator so each result can be
confirmed independently before the report is accepted. If Calculator does not
open, finish the comparison manually and record the checked expressions with
the report. Running only `python3 summarize.py` produces report text but does
not complete the desktop sign-off.
