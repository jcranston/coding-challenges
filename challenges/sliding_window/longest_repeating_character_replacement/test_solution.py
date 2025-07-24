from .solution import longest_repeating_character_replacement


def test_longest_repeating_character_replacement():
    s = "ABAB"
    k = 2
    expected = 4
    assert longest_repeating_character_replacement(s, k) == expected

    s = "AABABBA"
    k = 1
    expected = 4
    assert longest_repeating_character_replacement(s, k) == expected

    s = "AAAA"
    k = 2
    expected = 4
    assert longest_repeating_character_replacement(s, k) == expected

    s = "ABCD"
    k = 0
    expected = 1
    assert longest_repeating_character_replacement(s, k) == expected

    s = "AABACCAABBAA"
    k = 3
    expected = 8
    assert longest_repeating_character_replacement(s, k) == expected
