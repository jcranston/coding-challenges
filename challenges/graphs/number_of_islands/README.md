**LeetCode #200**  
**Tags:** depth-first search, breadth-first search, union find, matrix

# Number of Islands

## Problem
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

## Examples

**Example 1:**
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**
```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## Constraints
- m == number of rows in grid
- n == number of columns in grid
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'

## Clarifications & Assumptions
- An island is a group of '1's (land) connected 4-directionally (horizontal or vertical).
- The grid is surrounded by water ('0') on all edges.
- The input grid is not empty.
- The function should return an integer count of islands.
- The grid may contain no islands (all '0's), in which case return 0.
- All values in the grid are strings '0' or '1'. 