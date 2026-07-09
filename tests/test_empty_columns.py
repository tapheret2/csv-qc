from pathlib import Path
import tempfile
from csv_qc import profile_csv

def test_empty_columns_reported():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "t.csv"
        p.write_text("a,b\n1,\n2,\n", encoding="utf-8")
        rep = profile_csv(p)
        assert "empty_columns" in rep
        assert "b" in rep["empty_columns"]
