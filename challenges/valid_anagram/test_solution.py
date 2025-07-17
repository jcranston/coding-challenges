from .solution import valid_anagram


def test_valid_anagram_example():
    assert valid_anagram("anagram", "nagaram") is True
    assert valid_anagram("artist", "strait") is True
    assert valid_anagram("rat", "car") is False
