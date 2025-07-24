from .solution import merge


def test_merge_example():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_merge_all_from_nums2():
    nums1 = [0, 0, 0]
    nums2 = [1, 2, 3]
    merge(nums1, 0, nums2, 3)
    assert nums1 == [1, 2, 3]


def test_merge_all_from_nums1():
    nums1 = [1, 2, 3]
    nums2 = []
    merge(nums1, 3, nums2, 0)
    assert nums1 == [1, 2, 3]


def test_merge_interleaved():
    nums1 = [1, 4, 7, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 4, 5, 6, 7]
