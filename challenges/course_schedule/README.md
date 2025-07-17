# Course Schedule

## Problem
You are given a total of `numCourses` courses labeled from `0` to `numCourses - 1`. You are also given a list of prerequisite pairs `prerequisites` where `prerequisites[i] = [a, b]` indicates that to take course `a` you must first take course `b`.

Return `True` if it is possible to finish all courses. Otherwise, return `False`.

## Example
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: True
Explanation: You can take course 0 first, then course 1.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: False
Explanation: There is a cycle (0 -> 1 -> 0), so you cannot finish all courses.
```

## Constraints
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= a, b < numCourses

## Clarifications & Assumptions
- The input is a directed graph: each pair [a, b] means an edge from b to a.
- There may be duplicate prerequisite pairs.
- The function should return a boolean: `True` if all courses can be finished, otherwise `False`.
- There may be courses with no prerequisites.
- The graph may be disconnected.
- No self-loops (i.e., [a, a]) will appear in prerequisites.

## Input Format
- The function will receive two arguments:
    - `numCourses` (int): the total number of courses
    - `prerequisites` (List[List[int]]): the prerequisite pairs

## Output Format
- Return a boolean: `True` if all courses can be finished, otherwise `False`.

## Notes
- Watch for cycles in the prerequisite graph (cycle = impossible to finish all courses).
- Consider both BFS (Kahn's algorithm) and DFS approaches for cycle detection.
- Edge cases: no prerequisites, all courses independent, large graphs, duplicate pairs. 