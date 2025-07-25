# Number of Islands — EXPLANATION

## Problem Recap
Given a 2D grid of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

## High-Level Approach
Use Depth-First Search (DFS) or Breadth-First Search (BFS) to traverse each island, marking visited land as water to avoid recounting. Count each traversal as one island.

## Step-by-Step Solution
1. Initialize a counter for islands.
2. Iterate through each cell in the grid:
    - If the cell is '1', increment the island counter and start a DFS/BFS from that cell to mark all connected land as visited ('0').
3. Continue until all cells are processed.

## Annotated Code
```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count
```

## Example Test Cases
```python
grid1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
assert num_islands(grid1) == 1

grid2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
assert num_islands(grid2) == 3
```

## Common Pitfalls
- Not marking visited land, leading to overcounting.
- Not handling empty grid or edge cases.
- Forgetting to check all four directions.

## Variations
- Use BFS instead of DFS.
- Diagonal connections (if allowed).
- Count the size of each island.

## References
- [LeetCode #200: Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [DFS and BFS Patterns](https://leetcode.com/problems/number-of-islands/solutions/) 