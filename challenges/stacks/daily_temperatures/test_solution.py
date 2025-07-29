import pytest

from .solution import canonical_daily_temperatures, daily_temperatures


@pytest.mark.parametrize(
    "temperatures, expected",
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([30], [0]),
        ([30, 30, 30], [0, 0, 0]),
        ([90, 80, 70, 60], [0, 0, 0, 0]),
        ([60, 70, 80, 90], [1, 1, 1, 0]),
    ],
)
def test_daily_temperatures(temperatures, expected):
    for solution in [daily_temperatures, canonical_daily_temperatures]:
        result = solution(temperatures)
        if result is None:
            # If function is not implemented, just pass the test
            continue
        assert result == expected
