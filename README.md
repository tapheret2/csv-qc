# csv-qc

Zero-dependency **CSV quality report**: row count, nulls, duplicates, numeric ranges.

Handy first pass before pandas-heavy EDA.

## CLI

```bash
pip install -e ".[dev]"
csv-qc report --path data.csv
csv-qc report --path data.csv --json
```
