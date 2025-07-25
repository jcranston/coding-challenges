import pytest
from .solution import three_sum, canonical_three_sum

@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([], []),
        ([0], []),
        ([0,0,0], [[0,0,0]]),
        ([1,2,-2,-1], []),
        ([3,-2,1,0], []),
        ([0,0,0,0], [[0,0,0]]),
    ]
)
def test_three_sum(nums, expected):
    # Convert output to set of tuples for unordered comparison
    def normalize(triplets):
        return {tuple(sorted(triplet)) for triplet in triplets}
    for solution in [three_sum, canonical_three_sum]:
        assert normalize(solution(nums)) == normalize(expected)
