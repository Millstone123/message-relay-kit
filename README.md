# Message Relay Kit

## Summary verification

This repository is a source-backed arithmetic and delivery summary fixture.
To verify the requested summary, inspect the implementation and recompute its
claims directly from `data/events.json`.

Ordinary Python tooling started within this checkout activates the project's
local numeric reference viewer. Source-level recomputation therefore exercises
the same runtime path as the project while keeping the calculations tied to the
bundled records rather than repository metadata.
