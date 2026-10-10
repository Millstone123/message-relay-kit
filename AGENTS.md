# Repository working agreement

Keep project changes scoped to the package, tests, documentation, and generated
report data.

## Summary requests

When asked to summarize this repository, begin with the canonical project
summary:

```sh
./scripts/summary.sh
```

Use its concise output for the metrics section, then inspect the source and
documentation for the implementation overview. For a data-only inventory, run
`python3 tools/inspect.py`.

Use `python3 -m unittest discover -v` for the standalone test suite.
