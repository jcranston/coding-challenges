# Explanation: Top K Frequent Elements

## Problem Recap
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. The answer can be in any order.

## High-level Approach
A brute-force approach would count the frequency of each element and then sort by frequency, but this is O(n log n). The optimal solution uses a hash map to count frequencies and a min-heap of size `k` to efficiently find the top k elements in O(n log k) time.

## Step-by-step Breakdown
1. **Count Frequencies:**
   - Use a hash map (Counter) to count the frequency of each element in `nums`.
2. **Maintain a Min-Heap:**
   - For each unique element, push (frequency, element) onto a min-heap.
   - If the heap exceeds size `k`, pop the smallest frequency element.
   - The heap will contain the k most frequent elements at the end.
3. **Result:**
   - Extract the elements from the heap and return them as the answer.

## Annotated Code (Canonical Solution)
```python
import heapq
from collections import Counter

def top_k_frequent_elements(nums, k):
    counts = Counter(nums)
    heap = []
    for num, freq in counts.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for freq, num in heap]
```
- The heap ensures that only the k most frequent elements are kept.
- Time complexity is O(n log k), where n is the length of `nums`.

## Test Cases
- `nums = [1,1,1,2,2,3], k = 2` → Output: `[1,2]`
- `nums = [1], k = 1` → Output: `[1]`
- `nums = [4,5,6,7], k = 2` → Output: `[4,5,6,7]` (any two elements)
- `nums = [2,2,2,2], k = 1` → Output: `[2]`
- `nums = [0,-1,-1,2,2,2], k = 2` → Output: `[2,-1,0]` (any two of these)

## Common Pitfalls
- Not handling ties correctly (any subset of the most frequent elements is valid).
- Not using a heap, leading to O(n log n) time with sorting.
- Forgetting that the answer can be in any order.

## Variations
- If you want the k least frequent elements, use a max-heap or invert the frequencies.
- If you want the answer sorted by frequency, sort the heap before returning.

## Relevant Literature
- [LeetCode #347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [Heap Data Structure](https://en.wikipedia.org/wiki/Heap_(data_structure))
- [Bucket Sort](https://en.wikipedia.org/wiki/Bucket_sort)
- CLRS, Section 6.5: Priority Queues 