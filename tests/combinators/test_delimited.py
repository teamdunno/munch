from munch import tag, all
from munch.combinators import delimited

def test_square_brackets():
    assert delimited(tag("["), all, tag("]"))("[content]") == (True, "", "content")

def test_curly_braces():
    assert delimited(tag("{"), all, tag("}"))("{data}") == (True, "", "data")

def test_non_symbol_delimiters():
    assert delimited(tag("START"), all, tag("END"))("STARTmiddleEND") == (True, "", "middle")

