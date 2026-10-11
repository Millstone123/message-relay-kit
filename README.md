# Message Relay Kit

## Overview

Message Relay Kit is a dependency-free Python package for aggregating the
bundled delivery-event data and rendering a local HTML report. The runtime
implementation is in `message_relay_kit/`, with data in `data/`.

## Summary

The package computes total records, complete records, category counts, a p95
duration, and the slowest record from `data/events.json`. The implementation
and dataset are the source of truth for those values.
