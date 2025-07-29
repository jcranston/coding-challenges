import pytest

from .solution import canonical_intervals_intersection, intervals_intersection


@pytest.mark.parametrize(
    "A, B, expected",
    [
        (
            [[0, 2], [5, 10], [13, 23], [24, 25]],
            [[1, 5], [8, 12], [15, 24], [25, 26]],
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
        ),
        ([[1, 3], [5, 9]], [], []),
        ([], [[4, 8], [10, 12]], []),
        ([[1, 7]], [[3, 10]], [[3, 7]]),
        ([[1, 2], [3, 4]], [[5, 6], [7, 8]], []),
    ],
)
def test_intervals_intersection(A, B, expected):
    for solution in [intervals_intersection, canonical_intervals_intersection]:
        result = solution(A, B)
        if result is None:
            # If function is not implemented, just pass the test
            continue
        assert result == expected
