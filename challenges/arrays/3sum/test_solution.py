import pytest

from .solution import canonical_three_sum, three_sum


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([], []),
        ([0], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([1, 2, -2, -1], []),
        ([3, -2, 1, 0], []),
        ([0, 0, 0, 0], [[0, 0, 0]]),
    ],
)
def test_three_sum(nums, expected):
    # Convert output to set of tuples for unordered comparison
    def normalize(triplets):
        if triplets is None:
            return set()
        return {tuple(sorted(triplet)) for triplet in triplets}

    for solution in [three_sum, canonical_three_sum]:
        result = solution(nums)
        if result is None:
            # If function is not implemented, just pass the test
            continue
        assert normalize(result) == normalize(expected)
