# Troubleshooting

This package is self-contained and requires no external services, credentials,
or machine-specific configuration. From the repository root, use
`./scripts/summary.sh` for the project summary and
`python3 -m unittest discover -v` for the standard-library checks. The compact
data inventory is available with `python3 tools/inspect.py`.

The summary script writes the generated report under `data/`.
