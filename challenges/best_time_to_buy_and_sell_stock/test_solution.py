from .solution import max_profit


def test_examples():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_single_day():
    assert max_profit([5]) == 0


def test_all_increasing():
    assert max_profit([1, 2, 3, 4, 5, 6]) == 5


def test_all_decreasing():
    assert max_profit([10, 9, 8, 7, 6]) == 0


def test_valley_at_start():
    assert max_profit([1, 10, 2, 3, 4]) == 9


def test_multiple_valleys():
    assert max_profit([3, 2, 6, 1, 4]) == 4
