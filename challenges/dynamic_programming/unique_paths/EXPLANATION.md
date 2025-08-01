# Unique Paths - Detailed Explanation

## Problem Recap

The Unique Paths problem asks us to find the number of distinct paths from the top-left corner (0, 0) to the bottom-right corner (m-1, n-1) of an m×n grid, where we can only move right or down at each step. This is a classic dynamic programming problem that also has an elegant combinatorial solution.

**Key Constraints:**
- Grid dimensions: 1 ≤ m, n ≤ 100
- Movement: Only right or down allowed
- No obstacles in the grid
- Answer guaranteed to be ≤ 2×10^9

## High-Level Approach

There are two main approaches to solve this problem:

1. **Dynamic Programming (Top-down or Bottom-up)**: Build a solution by breaking down the problem into smaller subproblems, where each cell's value depends on the cells above and to the left.

2. **Combinatorial Mathematics**: Recognize that this is essentially a combination problem - we need to choose when to make right moves and when to make down moves.

The combinatorial approach is more efficient for this specific problem, while the DP approach is more generalizable to variations with obstacles.

## Step-by-Step Breakdown

### Dynamic Programming Approach

**Intuition:** The number of paths to reach any cell (i, j) equals the sum of paths to reach the cell above it (i-1, j) plus the paths to reach the cell to its left (i, j-1).

**Recurrence Relation:**
```
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

**Base Cases:**
- `dp[0][0] = 1` (starting point)
- `dp[0][j] = 1` for all j (top row - can only go right)
- `dp[i][0] = 1` for all i (leftmost column - can only go down)

**Implementation Details:**
- Use memoization to avoid recalculating subproblems
- Handle border cases separately (when i=0 or j=0)
- The final answer is `dp[m-1][n-1]`

### Combinatorial Approach

**Intuition:** To reach the bottom-right corner, we must make exactly (m-1) down moves and (n-1) right moves, in any order.

**Mathematical Insight:**
- Total moves needed: (m-1) + (n-1) = m+n-2
- We need to choose (m-1) positions out of (m+n-2) total positions for the down moves
- This is the combination: C(m+n-2, m-1)

**Why this works:** The order of moves doesn't matter - we just need to choose which steps will be down moves, and the rest will automatically be right moves.

## Annotated Code

### User Solution (Dynamic Programming with Memoization)

```python
def user_unique_paths(m: int, n: int) -> int:
    memo = {}

    def dp(x, y):
        if (x, y) in memo:
            return memo[(x, y)]

        # Base case: if we're at the start, there's 1 path
        if x == 0 and y == 0:
            return 1
        
        # Border cases: only recurse in valid directions
        if x == 0:  # At top border, can only go right
            result = dp(x, y - 1)
        elif y == 0:  # At left border, can only go down
            result = dp(x - 1, y)
        else:  # In middle, can go both directions
            result = dp(x - 1, y) + dp(x, y - 1)
        
        memo[(x, y)] = result
        return result
    
    # We want paths to (m-1, n-1) since grid is 0-indexed
    return dp(m - 1, n - 1)
```

**Key Points:**
- Uses memoization to avoid recalculating subproblems
- Handles border cases explicitly (when x=0 or y=0)
- Recursive approach with base case at (0,0)
- Time complexity: O(m×n), Space complexity: O(m×n)

### Canonical Solution (Combinatorial)

```python
def canonical_unique_paths(m: int, n: int) -> int:
    # Combinatorial approach: C(m+n-2, m-1)
    # We need to make (m-1) right moves and (n-1) down moves
    # Total moves = (m-1) + (n-1) = m+n-2
    # We choose (m-1) positions for right moves: C(m+n-2, m-1)
    
    def combination(n, k):
        """Calculate C(n,k) = n! / (k! * (n-k)!)"""
        if k > n - k:
            k = n - k  # Use symmetry
        
        result = 1
        for i in range(k):
            result = result * (n - i) // (i + 1)
        return result
    
    return combination(m + n - 2, m - 1)
```

**Key Points:**
- Uses the mathematical formula C(m+n-2, m-1)
- Implements combination calculation efficiently
- Avoids factorial overflow by using iterative multiplication
- Time complexity: O(min(m,n)), Space complexity: O(1)

## Test Case Analysis

Let's examine some key test cases to understand the patterns:

**Case 1: m=3, n=7, expected=28**
- Need 2 down moves and 6 right moves
- Total moves: 8
- C(8,2) = 8!/(2!×6!) = 28

**Case 2: m=3, n=2, expected=3**
- Need 2 down moves and 1 right move
- Total moves: 3
- C(3,2) = 3!/(2!×1!) = 3

**Case 3: m=1, n=1, expected=1**
- No moves needed (already at destination)
- C(0,0) = 1

**Case 4: m=2, n=2, expected=2**
- Need 1 down move and 1 right move
- Total moves: 2
- C(2,1) = 2!/(1!×1!) = 2

## Common Pitfalls

1. **Off-by-one errors**: Confusing 0-indexed vs 1-indexed coordinates
   - Solution: Always remember we're moving to (m-1, n-1)

2. **Incorrect base cases**: Not handling border cases properly
   - Solution: Explicitly handle when x=0 or y=0

3. **Overflow in combinatorial approach**: Using factorial directly
   - Solution: Use iterative multiplication and division

4. **Incorrect recurrence**: Adding wrong cells in DP
   - Solution: Always add the cell above and the cell to the left

5. **Memory issues**: Not using memoization in recursive DP
   - Solution: Use a dictionary to cache results

6. **Confusing the combination formula**: Using wrong parameters
   - Solution: Remember it's C(m+n-2, m-1), not C(m+n-2, n-1)

## Variations and Extensions

1. **Grid with Obstacles**: Add a grid parameter where some cells are blocked
   - Solution: Modify DP to skip blocked cells

2. **Different Movement Patterns**: Allow diagonal moves or more directions
   - Solution: Add more terms to the recurrence relation

3. **Weighted Paths**: Each move has a cost
   - Solution: Find minimum cost path instead of counting paths

4. **Multiple Destinations**: Find paths to multiple target cells
   - Solution: Use dynamic programming with multiple targets

5. **Large Grids**: When m and n are very large
   - Solution: Use the combinatorial approach to avoid memory issues

## Relevant Literature and Resources

1. **LeetCode Problem #62**: The original problem this is based on
   - https://leetcode.com/problems/unique-paths/

2. **Combinatorial Mathematics**: 
   - "Concrete Mathematics" by Graham, Knuth, and Patashnik
   - Chapter on combinations and binomial coefficients

3. **Dynamic Programming**:
   - "Introduction to Algorithms" (CLRS) - Chapter 15 on Dynamic Programming
   - Grid path problems are classic DP examples

4. **Mathematical Properties**:
   - Pascal's Triangle connection: The DP table forms Pascal's triangle
   - Binomial coefficient properties and efficient calculation

5. **Related Problems**:
   - Unique Paths II (with obstacles)
   - Minimum Path Sum
   - Robot Path Planning

## Time and Space Complexity

**Dynamic Programming Approach:**
- Time: O(m×n) - each cell is computed once
- Space: O(m×n) - memoization table

**Combinatorial Approach:**
- Time: O(min(m,n)) - computing combination
- Space: O(1) - constant extra space

The combinatorial approach is more efficient for this specific problem, especially for large grids, but the DP approach is more generalizable to variations with obstacles or different constraints. 