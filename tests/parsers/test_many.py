from munch import many, tag

def test_many_parses_multiple_tags():
    assert many(tag("A"))("AAAB") == (True, "B", ["A", "A", "A"])

def test_many_parses_no_tags():
    assert many(tag("A"))("BBB") == (True, "BBB", [])

def test_many_parses_empty_input():
    assert many(tag("A"))("") == (True, "", [])

def test_many_parses_partial_tags():
    assert many(tag("AB"))("ABABX") == (True, "X", ["AB", "AB"])

def test_many_with_different_tags():
    assert many(tag("X"))("XXYXX") == (True, "YXX", ["X", "X"])

