from pathlib import Path
import tempfile
from csv_qc.qc import row_count

def test_row_count():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "t.csv"
        p.write_text("a,b\n1,2\n3,4\n", encoding="utf-8")
        assert row_count(p) == 2
