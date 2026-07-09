# csv-qc

![status](https://img.shields.io/badge/status-active-brightgreen) ![python](https://img.shields.io/badge/python-3.10%2B-blue) ![license](https://img.shields.io/badge/license-MIT-lightgrey)

Zero-dependency **CSV quality report**: row count, nulls, duplicates, numeric ranges.

Handy first pass before pandas-heavy EDA.

## CLI

```bash
pip install -e ".[dev]"
csv-qc report --path data.csv
csv-qc report --path data.csv --json
```
