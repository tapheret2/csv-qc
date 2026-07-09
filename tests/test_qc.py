from pathlib import Path

from csv_qc import profile_csv


def test_profile_sample():
    p = Path(__file__).parent / "sample.csv"
    rep = profile_csv(p)
    assert rep["rows"] == 5
    assert rep["columns"] == 3
    null_result = next(f for f in rep["fields"] if f["column"] == "result")
    assert null_result["nulls"] == 1
