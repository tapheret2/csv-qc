from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .qc import profile_csv


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="csv-qc")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("report")
    r.add_argument("--path", type=Path, required=True)
    r.add_argument("--json", action="store_true")
    args = p.parse_args(argv)
    if args.cmd == "report":
        if not args.path.exists():
            print(f"missing file: {args.path}", file=sys.stderr)
            return 1
        rep = profile_csv(args.path)
        if args.json:
            print(json.dumps(rep, indent=2))
        else:
            print(f"rows={rep['rows']} cols={rep['columns']} dup_rows~={rep['duplicate_rows_approx']}")
            for f in rep["fields"]:
                line = f"  {f['column']}: nulls={f['nulls']} ({f['null_rate']:.1%})"
                if "mean" in f:
                    line += f" mean={f['mean']:.4g} [{f['min']:.4g}, {f['max']:.4g}]"
                print(line)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
