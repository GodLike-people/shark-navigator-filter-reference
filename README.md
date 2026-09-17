# Shark Navigator Filter Compatibility Reference

A small, reusable reference dataset and exact-match lookup for replacement filter kits used by selected Shark Navigator upright vacuums.

## What is included

- `data/shark-navigator-filter-compatibility.csv`: one model-to-kit mapping per row.
- `src/lookup.py`: a dependency-free command-line lookup tool.
- `docs/methodology.md`: scope, normalization rules, and provenance notes.

The data is intentionally conservative: a model is included only when it appears in the source compatibility lists captured for this reference. The lookup normalizes case, spaces, and hyphens, but does not infer compatibility from a model prefix or product family.

## Quick start

```text
python src/lookup.py NV-356E
```

The source lists were transcribed from official Shark product pages on September 15, 2026. Always confirm fit on the linked manufacturer page before ordering. The companion web reference is [Vacuum Parts Finder](https://vacuumpartsfinder.com/), an independent exact-model lookup.

## License

This dataset and code are released under the MIT License. Manufacturer names, trademarks, and product information remain the property of their respective owners.
