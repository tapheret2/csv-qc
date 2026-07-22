from csv_qc.qc import detect_delimiter, header_fingerprint

def test_detect_comma():
    assert detect_delimiter("a,b,c\n1,2,3") == ","

def test_detect_semicolon():
    assert detect_delimiter("a;b;c\n1;2;3") == ";"

def test_header_fingerprint():
    assert header_fingerprint(["Name", " Age "]) == "name|age"
