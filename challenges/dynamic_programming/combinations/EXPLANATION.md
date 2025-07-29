# Combinations (C(n,k)) - Dynamic Programming Explanation

## Problem Overview

The problem asks us to compute C(n,k), the number of ways to choose k items from n distinct items. This is a classic combinatorial problem that can be solved using dynamic programming.

## The Recurrence Relation

The key insight is the recurrence relation:
```
C(n,k) = C(n-1,k-1) + C(n-1,k)
```

## Intuition: "One Element In/Out" Principle

The core intuition comes from considering what happens to **one specific element** when we make our choice:

### Case 1: The element is INCLUDED in our selection
- If we include this element, we now need to choose **k-1** more elements from the remaining **n-1** elements
- This gives us `C(n-1, k-1)` ways

### Case 2: The element is EXCLUDED from our selection  
- If we exclude this element, we still need to choose **k** elements from the remaining **n-1** elements
- This gives us `C(n-1, k)` ways

### Why n-1?

The `n-1` appears because we're making a decision about **one specific element**:
- We've "used up" our decision-making power on this one element
- We're left with `n-1` elements to choose from
- This is the essence of the "divide and conquer" approach in dynamic programming

## Base Cases

1. **C(n,0) = 1**: There's exactly one way to choose 0 items from n items (choose nothing)
2. **C(n,n) = 1**: There's exactly one way to choose all n items from n items (choose everything)  
3. **C(n,k) = 0** when k > n: Impossible to choose more items than available

## Dynamic Programming Approaches

### Top-Down (Memoization)
- Start with the full problem C(n,k)
- Recursively break down using the recurrence
- Use memoization to avoid redundant calculations
- Natural recursive structure

### Bottom-Up (Tabulation)
- Build the solution from smaller subproblems
- Fill a table where dp[i][j] = C(i,j)
- Only need k+1 columns since we're computing up to C(n,k)
- Creates the relevant portion of Pascal's triangle

## Connection to Pascal's Triangle

The values C(n,k) form Pascal's triangle:
```
     C(0,0)
   C(1,0) C(1,1)
 C(2,0) C(2,1) C(2,2)
C(3,0) C(3,1) C(3,2) C(3,3)
```

Each entry is the sum of the two entries above it, which directly corresponds to our recurrence relation.

## Time and Space Complexity

- **Time**: O(n×k) - we fill a table of size n×k
- **Space**: O(n×k) - for the DP table

## Key Insight

The "one element in/out" principle is a powerful technique for developing recurrence relations in combinatorial problems. By focusing on the decision for a single element, we can systematically break down complex counting problems into simpler subproblems. 