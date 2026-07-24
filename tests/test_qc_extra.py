from csv_qc.qc import count_nullish, unique_ratio


def test_count_nullish():
    assert count_nullish([None, "", "  ", "x"]) == 3


def test_unique_ratio():
    assert unique_ratio(["a", "a", "b"]) == 2 / 3
