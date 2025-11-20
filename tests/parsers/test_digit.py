from munch import digit

def test_digit_parses_one():
    assert digit("5") == (True, "", "5")

def test_digit_fails_on_letter():
    assert digit("a") == (False, "a", "")

def test_digit_fails_on_empty():
    assert digit("") == (False, "", "")

def test_digit_fails_on_special_char():
    assert digit("@") == (False, "@", "")

def test_digit_fails_on_space():
    assert digit(" ") == (False, " ", "")

def test_digit_dosent_parse_multiple():
    assert digit("42") == (True, "2", "4")
