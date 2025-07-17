import heapq
from typing import Counter


def top_k_frequent_elements_user(nums, k):
    """
    User-submitted solution for the Top K Frequent Elements problem.
    Args:
        nums (List[int]): The input array.
        k (int): The number of most frequent elements to return.
    Returns:
        List[int]: The k most frequent elements in any order.
    """
    counts = Counter(nums)
    heap = []
    for num, freq in counts.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in heap]


def top_k_frequent_elements_canonical(nums, k):
    """
    Canonical solution for the Top K Frequent Elements problem (reference
    implementation).
    Args:
        nums (List[int]): The input array.
        k (int): The number of most frequent elements to return.
    Returns:
        List[int]: The k most frequent elements in any order.
    """
    import heapq
    from collections import Counter

    counts = Counter(nums)
    # Use a min-heap of size k
    heap = []
    for num, freq in counts.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for freq, num in heap]
