import pytest
from .solution import find_number_of_provinces, canonical_find_number_of_provinces


@pytest.mark.parametrize(
    "is_connected,expected",
    [
        ([[1,1,0],[1,1,0],[0,0,1]], 2),
        ([[1,0,0],[0,1,0],[0,0,1]], 3),
        ([[1]], 1),
        ([[1,1,1],[1,1,1],[1,1,1]], 1),
        ([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]], 1),
    ]
)
def test_number_of_provinces(is_connected, expected):
    for solution in [find_number_of_provinces, canonical_find_number_of_provinces]:
        assert solution(is_connected) == expected
