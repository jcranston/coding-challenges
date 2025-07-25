# Trapping Rain Water — EXPLANATION

## Problem Recap
Given n non-negative integers representing an elevation map, compute how much water it can trap after raining. Each bar has width 1.

## High-Level Approach
The optimal solution uses two pointers and tracks the maximum height to the left and right of each bar. Water can only be trapped where both sides are bounded by taller bars.

## Step-by-Step Solution
1. Initialize two pointers, `left` and `right`, at the start and end of the array.
2. Track `left_max` and `right_max`, the highest bars seen so far from each side.
3. Move the pointer with the lower bar inward:
    - If the current bar is less than the max on its side, water can be trapped above it.
    - Otherwise, update the max for that side.
4. Accumulate trapped water as you move the pointers.
5. Continue until the pointers meet.

## Annotated Code
```python
from typing import List

def trapping_rain_water_canonical(height: List[int]) -> int:
    if len(height) < 3:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water
```

## Example Test Cases
```python
assert trapping_rain_water_canonical([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert trapping_rain_water_canonical([4,2,0,3,2,5]) == 9
assert trapping_rain_water_canonical([]) == 0
```

## Common Pitfalls
- Not handling empty or very short arrays (should return 0).
- Forgetting to update left_max/right_max as you move pointers.
- Double-counting or missing trapped water at the edges.

## Variations
- Calculate trapped water for 2D elevation maps (harder).
- Return the indices of bars where water is trapped.

## References
- [LeetCode #42: Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
- [Two Pointer Pattern](https://leetcode.com/problems/trapping-rain-water/solutions/) 