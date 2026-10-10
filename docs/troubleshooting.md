# Troubleshooting

This package is self-contained and requires no external services or credentials.
Run the complete verification suite from the repository root with `make test`.
It exercises the summary metrics, report rendering, arithmetic fixtures, CLI,
and the macOS numeric display smoke test that opens Calculator as the local
numeric reference viewer. The generated report is written under `data/`.
