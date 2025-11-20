from typeguard import check_type
from munch import opt, tag
from munch.meta.types import MunchParser

def test_opt_generates_parser():
    check_type(opt(tag("TEST")), MunchParser)

def test_opt_parses_present_tag():
    assert opt(tag("TEST"))("TESTING") == (True, "ING", "TEST")

def test_opt_parses_absent_tag():
    assert opt(tag("TEST"))("FAIL") == (True, "FAIL", "")

def test_opt_parses_empty_input():
    assert opt(tag("TEST"))("") == (True, "", "")

def test_opt_with_different_tags():
    assert opt(tag("X"))("XY") == (True, "Y", "X")
