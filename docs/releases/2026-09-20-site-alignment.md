# Scope: 68 exact model mappings — XFF350 + XHF350 (51) and XFF500 + XHF500 (17)

This release aligns `data/shark-navigator-filter-compatibility.csv` to the two exact-model lists rendered by [Vacuum Parts Finder](https://vacuumpartsfinder.com/) on 2026-09-20.

Measured comparison:

- Site coverage: 68 rows, split 51 + 17.
- Dataset before alignment: 45 rows, split 29 + 16.
- Site-only rows added: 23, all in `XFF350 + XHF350` except `ZU782NP` in `XFF500 + XHF500`.
- Dataset-only rows: 0.
- Dataset after alignment: 68 rows, split 51 + 17.

The 23 added rows use the official source URL already associated with their site filter group:

- `XFF350 + XHF350`: https://www.sharkclean.com/products/foam-felt-filter-kit-zidXFF350?modelNumber=NV356E
- `XFF500 + XHF500`: https://www.sharkclean.com/products/pre-motor-filter-kit-zidXFF500?modelNumber=ZU785

The site lists are the authority for this alignment; no dataset-only model was deleted and no model was inferred or invented.
