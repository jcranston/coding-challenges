from .solution import sliding_window_maximum


def test_sliding_window_maximum():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    expected = [3, 3, 5, 5, 6, 7]
    assert sliding_window_maximum(nums, k) == expected

    nums = [1]
    k = 1
    expected = [1]
    assert sliding_window_maximum(nums, k) == expected

    nums = [9, 11]
    k = 2
    expected = [11]
    assert sliding_window_maximum(nums, k) == expected

    nums = [4, 3, 2, 1]
    k = 2
    expected = [4, 3, 2]
    assert sliding_window_maximum(nums, k) == expected
