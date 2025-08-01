# Unique Paths

## Problem Description

You are given an `m x n` grid. You are initially positioned at the top-left corner (0, 0) and need to reach the bottom-right corner (m-1, n-1). You can only move either down or right at any point in time.

Return the number of possible unique paths that you can take to reach the bottom-right corner.

## Examples

### Example 1:
```
Input: m = 3, n = 7
Output: 28
Explanation: There are 28 unique paths from (0,0) to (2,6)
```

### Example 2:
```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right  
3. Down -> Right -> Down
```

### Example 3:
```
Input: m = 7, n = 3
Output: 28
```

### Example 4:
```
Input: m = 3, n = 3
Output: 6
```

## Constraints

- `1 <= m, n <= 100`
- It's guaranteed that the answer will be less than or equal to 2 * 10^9

## Clarifications

- You can only move right or down at each step
- You must stay within the grid boundaries
- The grid is empty (no obstacles)
- The starting position is always (0, 0) and the target is always (m-1, n-1)

## Notes

This problem can be solved using:
1. **Dynamic Programming**: Build a 2D DP table where dp[i][j] represents the number of paths to reach cell (i,j)
2. **Combinatorial Mathematics**: The answer is C(m+n-2, m-1) or C(m+n-2, n-1), since you need to make exactly (m-1) right moves and (n-1) down moves in any order

The combinatorial approach is more efficient for this specific problem, but the DP approach is more generalizable to variations with obstacles or different constraints. 