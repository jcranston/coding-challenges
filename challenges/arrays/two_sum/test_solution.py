from .solution import solve


def test_example():
    assert set(solve([2, 7, 11, 15], 9)) == {0, 1}


def test_negative_numbers():
    assert set(solve([-3, 4, 3, 90], 0)) == {0, 2}


def test_duplicates():
    assert set(solve([3, 3], 6)) == {0, 1}


def test_large_numbers():
    assert set(solve([1000000000, 299, 1, -999999999], 1)) == {0, 3}


def test_no_solution():
    # According to the problem, there is always exactly one solution, so this is
    # just for completeness
    assert solve([1, 2, 3], 7) == []
