# Explanation: Subarray Sum Equals K

## Problem Recap
Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals `k`. Subarrays must be contiguous, and values in `nums` can be negative, zero, or positive.

## High-level Approach
A brute-force approach would check all possible subarrays, but this is inefficient for large arrays. Instead, we use prefix sums and a hash map to efficiently count the number of subarrays that sum to `k` in linear time.

## Step-by-step Breakdown
1. **Prefix Sums:**
   - The prefix sum at index `i` is the sum of all elements up to (and including) `i`.
2. **Hash Map:**
   - Use a hash map to store the frequency of each prefix sum encountered so far.
   - For each index, check if there is a previous prefix sum such that the difference between the current prefix sum and `k` exists in the map. If so, increment the count by the frequency of that prefix sum.
3. **Iterate Through Array:**
   - Update the prefix sum and hash map as you iterate, counting valid subarrays as you go.

## Annotated Code
```python
from collections import defaultdict

def subarray_sum_equals_k(nums, k):
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1
    prefix_sum = 0
    count = 0
    for num in nums:
        prefix_sum += num
        count += prefix_sums[prefix_sum - k]
        prefix_sums[prefix_sum] += 1
    return count
```
- The hash map allows us to efficiently check for all subarrays ending at the current index whose sum is `k`.
- Initializing `prefix_sums[0] = 1` handles the case where a subarray starting from index 0 sums to `k`.

## Test Cases
- `nums = [1, 2, 3], k = 3` → Output: 2 (subarrays `[1,2]` and `[3]`)
- Edge cases to consider: all zeros, all negatives, `k = 0`, overlapping subarrays.

## Common Pitfalls
- Not initializing the hash map with `prefix_sums[0] = 1` (misses subarrays starting at index 0).
- Forgetting to handle negative numbers or zero in the array.
- Counting overlapping subarrays incorrectly.

## Variations
- If the problem asked for the longest subarray with sum `k`, a different approach would be needed (e.g., storing indices).
- If only positive numbers are allowed, a sliding window approach could be used.

## Relevant Literature
- [LeetCode #560: Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
- [Prefix Sum and Hash Map Techniques](https://leetcode.com/problems/subarray-sum-equals-k/solutions/)
- CLRS, Section 14.1: Prefix Sums 