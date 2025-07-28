# from .solution import kth_largest_element_canonical, kth_largest_element_user
from .solution import kth_largest_element


def test_kth_largest_element():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    expected = 5
    assert kth_largest_element(nums, k) == expected

    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    expected2 = 4
    assert kth_largest_element(nums2, k2) == expected2
