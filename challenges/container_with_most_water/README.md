# Container With Most Water

## Problem Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines, which, together with the x-axis, form a container that can hold the maximum amount of water.

Return the maximum amount of water a container can store.

## Examples

### Example 1:
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The maximum area is obtained by choosing height[1] = 8 and height[8] = 7.
The width is 8 - 1 = 7, and the height is min(8, 7) = 7.
Area = 7 * 7 = 49.
```

### Example 2:
```
Input: height = [1,1]
Output: 1
```

## Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Approach

### Key Insights:
1. The area of water contained between two lines is: `width × min(height[left], height[right])`
2. The width is the distance between the two lines: `right - left`
3. The height is limited by the shorter of the two lines

### Algorithm:
1. Use two pointers: one at the beginning and one at the end
2. Calculate the area between the two pointers
3. Move the pointer with the shorter height inward
4. Keep track of the maximum area found

### Why This Works:
- If we have a taller line on one side, moving the shorter line inward might give us a better area
- If we have equal heights, moving either pointer works
- We don't need to check all possible pairs because we can eliminate certain combinations

## Time and Space Complexity

- **Time Complexity:** O(n) - we only need one pass through the array
- **Space Complexity:** O(1) - we only use a constant amount of extra space

## Test Cases

The solution should handle:
- Arrays with all equal heights
- Arrays with increasing/decreasing heights
- Arrays with only two elements
- Arrays with very large heights
- Arrays with zero heights

## Hints

1. Think about what happens when you move the pointer with the shorter height
2. Consider why you don't need to check all possible pairs
3. What determines the maximum possible area for a given width? 