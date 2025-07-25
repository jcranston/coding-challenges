import pytest
from .solution import decode_string, canonical_decode_string

@pytest.mark.parametrize(
    "s,expected",
    [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("abc3[cd]xyz", "abccdcdcdxyz"),
        ("10[a]", "aaaaaaaaaa"),
        ("2[3[a]b]", "aaabaaab"),
        ("", ""),
        ("a", "a"),
    ]
)
def test_decode_string(s, expected):
    for solution in [decode_string, canonical_decode_string]:
        assert solution(s) == expected
