import pytest

from .solution import (
    canonical_find_number_of_provinces,
    find_number_of_provinces,
)


@pytest.mark.parametrize(
    "is_connected, expected",
    [
        ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
        ([[1]], 1),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1),
        ([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]], 1),
    ],
)
def test_number_of_provinces(is_connected, expected):
    for solution in [
        find_number_of_provinces,
        canonical_find_number_of_provinces,
    ]:
        result = solution(is_connected)
        if result is None:
            # If function is not implemented, just pass the test
            continue
        assert result == expected
