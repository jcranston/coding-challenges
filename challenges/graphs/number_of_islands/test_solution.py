import pytest

from .solution import canonical_num_islands, user_num_islands

test_cases = [
    # Example 1
    (
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        1,
    ),
    # Example 2
    (
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        3,
    ),
    # All water
    ([["0", "0", "0"], ["0", "0", "0"]], 0),
    # All land
    ([["1", "1"], ["1", "1"]], 1),
    # Single cell island
    ([["1"]], 1),
    # Single cell water
    ([["0"]], 0),
]


@pytest.mark.parametrize("grid, expected", test_cases)
def test_num_islands(grid, expected):
    for solution in [user_num_islands, canonical_num_islands]:
        assert solution([row[:] for row in grid]) == expected
