# Explanation: Container With Most Water

## Problem Recap
Given an array `height` representing the heights of vertical lines drawn at each index, find two lines that, together with the x-axis, form a container that holds the maximum amount of water. Return the maximum area of water a container can store.

## High-level Approach
The brute-force approach would check all pairs of lines, but this is inefficient for large arrays. Instead, we use a two-pointer technique to efficiently find the maximum area in a single pass.

## Step-by-step Breakdown
1. **Two Pointers:**
   - Start with one pointer at the beginning (`lp`) and one at the end (`rp`) of the array.
2. **Calculate Area:**
   - The area between the two lines is `min(height[lp], height[rp]) * (rp - lp)`.
3. **Move the Shorter Line:**
   - Move the pointer pointing to the shorter line inward, since the area is limited by the shorter line. This gives a chance to find a taller line and potentially a larger area.
4. **Track Maximum:**
   - Keep track of the maximum area found during the process.
5. **Repeat:**
   - Continue until the two pointers meet.

## Annotated Code
```python
from typing import List

def find_max_water_container_area(height: List[int]) -> int:
    lp = 0
    rp = len(height) - 1
    max_height = 0
    while lp < rp:
        max_height = max(max_height, min(height[lp], height[rp]) * (rp - lp))
        if height[lp] < height[rp]:
            lp += 1
        else:
            rp -= 1
    return max_height
```
- The two-pointer approach ensures every possible width is considered, and always moves toward a potentially taller line.
- The time complexity is O(n), and space complexity is O(1).

## Test Cases
- `[1, 8, 6, 2, 5, 4, 8, 3, 7]` → Output: 49
- `[1, 1]` → Output: 1
- `[4, 3, 2, 1, 4]` → Output: 16
- See `test_solution.py` for additional edge cases: all equal heights, increasing/decreasing heights, zeros, large numbers, alternating heights, and more.

## Common Pitfalls
- Moving the wrong pointer (should always move the one pointing to the shorter line).
- Not considering the case where both lines are of equal height (either pointer can be moved).
- Forgetting to update the maximum area at each step.

## Variations
- If the problem asked for the minimum area, a different approach would be needed.
- If the lines could be rearranged, the problem would change fundamentally.

## Relevant Literature
- [LeetCode #11: Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- [Two Pointer Technique](https://leetcode.com/tag/two-pointers/)
- CLRS, Section 14.1: Greedy Algorithms 