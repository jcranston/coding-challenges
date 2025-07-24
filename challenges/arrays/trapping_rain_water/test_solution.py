import pytest

from .solution import trapping_rain_water_canonical, trapping_rain_water_user


@pytest.mark.parametrize(
    "height, expected",
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([2, 0, 2], 2),
        ([3, 0, 0, 2, 0, 4], 10),
        ([0, 0, 0, 0], 0),
        ([1, 2, 3, 4, 5], 0),
        ([5, 4, 1, 2], 1),
        ([2, 1, 0, 2], 3),
        ([], 0),
    ],
)
def test_trapping_rain_water(height, expected):
    for solution in [trapping_rain_water_user, trapping_rain_water_canonical]:
        assert solution(height) == expected
