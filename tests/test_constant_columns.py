from pathlib import Path
import tempfile
from csv_qc.qc import constant_columns

def test_constant_columns_detects_static():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "t.csv"
        p.write_text("a,b\n1,x\n2,x\n3,x\n", encoding="utf-8")
        cols = constant_columns(p)
        assert "b" in cols
        assert "a" not in cols
