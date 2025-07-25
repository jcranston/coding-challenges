import pytest
from .solution import min_meeting_rooms, canonical_min_meeting_rooms

@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([[0,30],[5,10],[15,20]], 2),
        ([[7,10],[2,4]], 1),
        ([[1,5],[2,6],[3,7],[4,8]], 4),
        ([[1,2],[2,3],[3,4]], 1),
        ([[1,10],[2,3],[4,5],[6,7],[8,9]], 2),
        ([[1,2]], 1),
        ([[1,5],[5,10],[10,15]], 1),
    ]
)
def test_min_meeting_rooms(intervals, expected):
    for solution in [min_meeting_rooms, canonical_min_meeting_rooms]:
        assert solution(intervals) == expected
