from munch import alt, digit, letter
from munch.meta.types import MunchParser
from typeguard import check_type

def test_alt_generates_parser():
    check_type(alt(letter, digit), MunchParser)

def test_alt_parses_letter():
    assert alt(letter, digit)("a") == (True, "", "a")

def test_alt_parses_digit():
    assert alt(letter, digit)("7") == (True, "", "7")

def test_alt_fails_on_special_char():
    assert alt(letter, digit)("@") == (False, "@", "")

def test_alt_fails_on_empty():
    assert alt(letter, digit)("") == (False, "", "")
