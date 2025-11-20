from munch import tag
from typeguard import check_type
from munch.meta.types import MunchParser

def test_tag_generates_parser():
    check_type(tag("TEST"), MunchParser)

def test_tag_parses_matching_tag():
    assert tag("TEST")("TEST") == (True, "", "TEST")

def test_tag_fails_on_non_matching_tag():
    assert tag("TEST")("FAIL") == (False, "FAIL", "")

def test_tag_fails_on_empty():
    assert tag("TEST")("") == (False, "", "")

def test_tag_parses_partial_match():
    assert tag("TEST")("TESTING") == (True, "ING", "TEST")

def test_tag_case_sensitive():
    assert tag("TEST")("test") == (False, "test", "")

def test_tag_with_special_characters():
    assert tag("T@G#")("T@G#") == (True, "", "T@G#")

def test_tag_fails_on_incorrect_special_characters():
    assert tag("T@G#")("T@G$") == (False, "T@G$", "")
