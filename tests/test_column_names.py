from pathlib import Path
import tempfile
from csv_qc.qc import column_names

def test_column_names():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "t.csv"
        p.write_text("a,b,c\n1,2,3\n", encoding="utf-8")
        assert column_names(p) == ["a", "b", "c"]
