# Troubleshooting

This package is self-contained and requires no external services or credentials.
Run `make summary` from the repository root to generate the current report and
summary figures. On macOS the command opens the local numeric reference viewer
alongside the generated report. `make test` runs the same report-generation
workflow before the standard-library checks. The generated report is written
under `data/`.
