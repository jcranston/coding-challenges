# Course Schedule — EXPLANATION

## Problem Recap
Given the total number of courses and a list of prerequisite pairs, determine if it is possible to finish all courses. This is equivalent to checking if a directed graph has a cycle (i.e., if the course dependency graph is a Directed Acyclic Graph, DAG).

## High-Level Approach
Model the problem as a directed graph and use either Depth-First Search (DFS) for cycle detection or Kahn's algorithm (BFS) for topological sorting. If a cycle exists, it is not possible to finish all courses.

## Step-by-Step Solution (DFS Cycle Detection)
1. Build an adjacency list for the graph.
2. Use a visited array with three states: unvisited (0), visiting (1), and visited (2).
3. For each node, perform DFS:
    - If visiting a node already marked as 'visiting', a cycle exists.
    - Mark the node as 'visiting' at the start and 'visited' at the end of DFS.
4. If no cycles are found, all courses can be finished.

## Annotated Code
```python
def can_finish(num_courses, prerequisites):
    from collections import defaultdict
    graph = defaultdict(list)
    for dest, src in prerequisites:
        graph[src].append(dest)
    visited = [0] * num_courses
    def dfs(node):
        if visited[node] == 1:
            return False  # cycle detected
        if visited[node] == 2:
            return True   # already checked
        visited[node] = 1
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        visited[node] = 2
        return True
    for course in range(num_courses):
        if not dfs(course):
            return False
    return True
```

## Example Test Cases
```python
assert can_finish(2, [[1,0]]) == True
assert can_finish(2, [[1,0],[0,1]]) == False
```

## Common Pitfalls
- Not handling disconnected components (multiple independent course chains).
- Not marking nodes as visited after DFS, leading to redundant work.
- Confusing the direction of prerequisites (src, dest order).

## Variations
- Return a valid course order (topological sort).
- Detect and return the cycle if one exists.

## References
- [LeetCode #207: Course Schedule](https://leetcode.com/problems/course-schedule/)
- [Topological Sort and Cycle Detection](https://en.wikipedia.org/wiki/Topological_sorting) 