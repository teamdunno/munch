from munch import letter

def test_letter_parses_one():
    assert letter("a") == (True, "", "a")

def test_letter_fails_on_digit():
    assert letter("5") == (False, "5", "")

def test_letter_fails_on_empty():
    assert letter("") == (False, "", "")

def test_letter_fails_on_special_char():
    assert letter("@") == (False, "@", "")

def test_letter_fails_on_space():
    assert letter(" ") == (False, " ", "")

def test_letter_doesnt_parse_multiple():
    assert letter("ab") == (True, "b", "a")

def test_letter_parses_uppercase():
    assert letter("Z") == (True, "", "Z")

def test_letter_parses_mixed():
    assert letter("m3") == (True, "3", "m")

def test_letter_fails_on_newline():
    assert letter("\n") == (False, "\n", "")
