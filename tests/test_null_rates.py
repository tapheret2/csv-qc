from pathlib import Path
import tempfile
from csv_qc import null_rates

def test_null_rates_on_partial_column():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "t.csv"
        p.write_text("a,b\n1,x\n2,\n", encoding="utf-8")
        rates = null_rates(p)
        assert rates["a"] == 0.0
        assert rates["b"] > 0.0
