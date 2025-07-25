**LeetCode #547**  
**Tags:** graph, depth-first search, breadth-first search, union find

# Number of Provinces

## Problem
Given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and 0 otherwise, return the number of provinces.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

## Examples

### Example 1
```
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

### Example 2
```
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```

## Constraints
- 1 <= n <= 200
- isConnected[i][j] is 1 or 0
- isConnected[i][i] == 1
- isConnected[i][j] == isConnected[j][i]

## Clarifications & Assumptions
- Each city is connected to itself.
- The matrix is symmetric.
- A province is a maximal set of cities that are directly or indirectly connected.
- The answer is the number of such groups.

## Approach
- Model the cities as nodes in an undirected graph.
- Use DFS, BFS, or Union Find to count the number of connected components (provinces).
- For each unvisited city, start a traversal to mark all cities in its province.
- Increment the province count for each traversal.

## Notes
- Edge cases: single city, all cities connected, all cities disconnected.
- Efficient solutions should run in O(n^2) time.
- This problem is also known as "Connected Components in an Undirected Graph." 