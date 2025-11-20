from munch.combinators import int

def test_int_parses():
    assert int("12345") == (True, "", 12345)

def test_int_parses_zero():
    assert int("0") == (True, "", 0)

def test_int_fails_on_non_integer():
    assert int("abc") == (False, "abc", 0)

def test_int_fails_on_empty_string():
    assert int("") == (False, "", 0)

def test_int_parses_integer_with_trailing_characters():
    assert int("42xyz") == (True, "xyz", 42)

def test_int_dosent_parse_float():
    assert int("3.14") == (True, ".14", 3)

