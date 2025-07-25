# Explanation: Number of Provinces (LeetCode 547)

## Problem Recap
Given an n x n adjacency matrix `isConnected`, where `isConnected[i][j] = 1` if city i and city j are directly connected and 0 otherwise, return the number of provinces (groups of directly or indirectly connected cities).

A province is a maximal set of cities that are directly or indirectly connected. The matrix is symmetric, and each city is connected to itself.

## High-Level Approach
This problem is equivalent to finding the number of connected components in an undirected graph. Each city is a node, and a direct connection is an edge. We can use Depth-First Search (DFS), Breadth-First Search (BFS), or Union Find to count the number of connected components (provinces).

## Step-by-Step Breakdown (DFS)
1. **Initialization:**
   - Create a `visited` set to track which cities have been visited.
   - Initialize a `province_count` to 0.
2. **Iterate through each city:**
   - For each unvisited city, start a DFS traversal to mark all cities in its province as visited.
   - Increment `province_count` for each new traversal.
3. **DFS Traversal:**
   - For the current city, mark it as visited.
   - Recursively visit all directly connected, unvisited cities.
4. **Result:**
   - After all cities are processed, `province_count` is the answer.

## Annotated Canonical Solution (DFS)
```python
from typing import List

def canonical_find_number_of_provinces(is_connected: List[List[int]]) -> int:
    n = len(is_connected)
    visited = set()
    def dfs(city):
        for neighbor in range(n):
            if is_connected[city][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)
    province_count = 0
    for city in range(n):
        if city not in visited:
            visited.add(city)
            dfs(city)
            province_count += 1
    return province_count
```
- **Why this works:** Each DFS traversal marks all cities in a province as visited. The number of times we start a new DFS equals the number of provinces.

## Test Cases & Edge Cases
- `[[1,1,0],[1,1,0],[0,0,1]]` → `2` (two provinces)
- `[[1,0,0],[0,1,0],[0,0,1]]` → `3` (three provinces)
- `[[1]]` → `1` (single city)
- `[[1,1,1],[1,1,1],[1,1,1]]` → `1` (all cities connected)
- `[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]` → `1` (complex connection)

## Common Pitfalls
- Not marking cities as visited, leading to infinite recursion or overcounting.
- Forgetting that the matrix is symmetric and each city is connected to itself.
- Not handling single-city or fully disconnected cases.

## Variations
- **Union Find:** Can be used for more efficient solutions, especially for large graphs.
- **BFS:** An iterative alternative to DFS.
- **Different input formats:** Sometimes the problem is given as an edge list instead of an adjacency matrix.

## Relevant Literature
- [LeetCode 547: Number of Provinces](https://leetcode.com/problems/number-of-provinces/)
- [Connected Components - CLRS, Chapter 22](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)
- [DFS and BFS - Standard Graph Traversal Algorithms](https://en.wikipedia.org/wiki/Depth-first_search)
- [Union Find (Disjoint Set Union)](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)

---
This explanation references the problem statement, canonical solution, and test cases, and follows the conventions in `ai_context/explanation_generation.md`. 