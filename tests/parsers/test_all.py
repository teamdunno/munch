from munch import all

def test_all_nothing_returns_nothing():
    assert all("") == (True, "", "")

def test_all_returns_all():
    assert all("abc") == (True, "", "abc")

def test_all_always_succeeds():
    assert all("xyz") == (True, "", "xyz")
    assert all("123") == (True, "", "123")
    assert all("!@#") == (True, "", "!@#")
    assert all(" ") == (True, "", " ")
    assert all("\n") == (True, "", "\n")

