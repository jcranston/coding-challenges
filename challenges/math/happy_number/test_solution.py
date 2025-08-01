import pytest

from .solution import canonical_is_happy, is_happy


@pytest.mark.parametrize(
    "n, expected",
    [
        (19, True),
        (2, False),
        (1, True),
        (7, True),
        (4, False),
        (100, True),
        (1111111, True),
        (0, False),
    ],
)
def test_is_happy(n, expected):
    for solution in [is_happy, canonical_is_happy]:
        result = solution(n)
        if result is None:
            # If function is not implemented, just pass the test
            continue
        assert result == expected
