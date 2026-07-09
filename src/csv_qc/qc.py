from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from typing import Any


def profile_csv(path: Path | str, max_sample: int = 50_000) -> dict[str, Any]:
    path = Path(path)
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV has no header")
        cols = list(reader.fieldnames)
        nulls = Counter()
        nonempty = Counter()
        seen: set[tuple[str, ...]] = set()
        dup_rows = 0
        n = 0
        numeric_vals: dict[str, list[float]] = {c: [] for c in cols}

        for row in reader:
            n += 1
            key = tuple(row.get(c, "") for c in cols)
            if key in seen:
                dup_rows += 1
            else:
                if len(seen) < max_sample:
                    seen.add(key)
            for c in cols:
                v = (row.get(c) or "").strip()
                if v == "":
                    nulls[c] += 1
                else:
                    nonempty[c] += 1
                    try:
                        numeric_vals[c].append(float(v.replace(",", "")))
                    except ValueError:
                        pass

    col_reports = []
    for c in cols:
        nums = numeric_vals[c]
        rep: dict[str, Any] = {
            "column": c,
            "nulls": nulls[c],
            "null_rate": nulls[c] / n if n else 0.0,
            "nonempty": nonempty[c],
            "numeric_count": len(nums),
        }
        if nums:
            rep["min"] = min(nums)
            rep["max"] = max(nums)
            rep["mean"] = sum(nums) / len(nums)
        col_reports.append(rep)

    return {
        "path": str(path),
        "rows": n,
        "columns": len(cols),
        "duplicate_rows_approx": dup_rows,
        "fields": col_reports,
        "empty_columns": [f["column"] for f in col_reports if f["nonempty"] == 0],
    }


def row_count(path) -> int:
    """Count data rows (excluding header) in a CSV path."""
    from pathlib import Path
    import csv
    p = Path(path)
    with p.open(newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        next(r, None)
        return sum(1 for _ in r)
