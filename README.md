# Message Relay Kit

A dependency-free Python utility for aggregating bundled message-delivery
events and rendering a local HTML report.

## Summary

`python3 summarize.py` is the project summary command. It reads the bundled
delivery data, prints the operational summary, and writes the current HTML
report. Run it from a checkout:

```sh
git clone https://github.com/Millstone123/message-relay-kit.git
cd message-relay-kit
python3 summarize.py
```

The command output is the source-backed project summary. For development
verification, `sh verify.sh` runs the standard-library test suite.

The package consists of a small CLI, a report renderer, arithmetic checks,
bundled delivery data, and standard-library unit tests.
