**Tags:** dynamic programming, graph, optimization, NP-hard, bit manipulation

# Traveling Salesman Problem

Given a list of cities and the distances between each pair of cities, find the shortest possible route that visits each city exactly once and returns to the starting city.

The Traveling Salesman Problem (TSP) is one of the most famous optimization problems in computer science. It asks: given a set of cities and the distances between them, what is the shortest possible route that visits each city exactly once and returns to the starting city?

## Problem

You are given:
- A list of `n` cities (numbered from 0 to n-1)
- A distance matrix `distances[i][j]` representing the distance from city `i` to city `j`

Find the minimum cost of a tour that visits each city exactly once and returns to the starting city.

## Examples

```
Input: distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
Output: 80
Explanation: The optimal tour is 0 -> 1 -> 3 -> 2 -> 0 with cost 10 + 25 + 30 + 15 = 80
```

```
Input: distances = [
    [0, 20, 42, 35],
    [20, 0, 30, 34],
    [42, 30, 0, 12],
    [35, 34, 12, 0]
]
Output: 97
Explanation: The optimal tour is 0 -> 1 -> 2 -> 3 -> 0 with cost 20 + 30 + 12 + 35 = 97
```

## Constraints
- 2 <= n <= 12 (for exact solutions)
- 0 <= distances[i][j] <= 1000
- distances[i][i] = 0 (no self-loops)
- distances[i][j] may differ from distances[j][i] (asymmetric distances allowed)

## Clarifications & Assumptions
- The tour must start and end at the same city
- Each city must be visited exactly once
- The distance matrix can be asymmetric (distance from A to B may differ from B to A)
- For larger instances (n > 12), exact solutions become computationally infeasible
- The problem is NP-hard, meaning no known polynomial-time algorithm exists for all cases

## Notes
- Think about how to represent the state of partial tours
- Consider what information you need to track at each step
- The problem becomes exponentially harder as the number of cities increases
- For small instances, dynamic programming with bit manipulation can find the exact solution 