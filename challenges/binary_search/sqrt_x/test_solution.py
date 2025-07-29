import pytest

from .solution import canonical_sqrt_x, user_sqrt_x


@pytest.mark.parametrize(
    "x, expected",
    [
        (0, 0),
        (1, 1),
        (4, 2),
        (8, 2),
        (9, 3),
        (15, 3),
        (16, 4),
        (2147395599, 46339),  # large x
    ],
)
def test_sqrt_x(x, expected):
    for solution in [user_sqrt_x, canonical_sqrt_x]:
        assert solution(x) == expected
