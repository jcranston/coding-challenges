import pytest
from .solution import is_happy, canonical_is_happy

@pytest.mark.parametrize(
    "n,expected",
    [
        (19, True),
        (2, False),
        (1, True),
        (7, True),
        (4, False),
        (100, True),
        (1111111, True),
        (0, False),
    ]
)
def test_is_happy(n, expected):
    for solution in [is_happy, canonical_is_happy]:
        assert solution(n) == expected
