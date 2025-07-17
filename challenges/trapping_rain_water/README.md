# Trapping Rain Water

## Problem
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Examples
- Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
  Output: 6
  Explanation: The above elevation map (represented by array) can trap 6 units of water.

- Input: height = [4,2,0,3,2,5]
  Output: 9

## Constraints
- 0 <= n <= 3 * 10^4
- 0 <= height[i] <= 10^5

## Clarifications / Assumptions
- The input array may be empty; return 0 in that case.
- All values in the array are non-negative integers.
- The width of each bar is 1.
- Water cannot be trapped at the edges if there is no boundary.
- Return the total amount of trapped water as an integer. 