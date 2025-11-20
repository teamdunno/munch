from munch import tag
from munch.combinators import between

def test_html_tag():
    parser = between(tag("<"), tag(">"))
    assert parser("<div>") == (True, "", "div")

def test_html_tag_with_content():
    parser = between(tag("<"), tag(">"))
    assert parser("<span>content</span>") == (True, "content</span>", "span")

def test_parentheses():
    parser = between(tag("("), tag(")"))
    assert parser("(inside)") == (True, "", "inside")
