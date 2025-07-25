# Explanation: Edit Distance

## Problem Recap
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`. Allowed operations are insert, delete, or replace a character.

## High-level Approach
This is a classic dynamic programming problem. The key idea is to use a 2D DP table where `dp[i][j]` represents the minimum edit distance between the first `i` characters of `word1` and the first `j` characters of `word2`.

## Step-by-step Breakdown
1. **DP Table Definition:**
   - Let `dp[i][j]` be the minimum number of operations to convert `word1[:i]` to `word2[:j]`.
2. **Base Cases:**
   - `dp[0][j] = j` (convert empty string to first `j` chars of `word2` by inserting all `j` chars)
   - `dp[i][0] = i` (convert first `i` chars of `word1` to empty string by deleting all `i` chars)
3. **DP Transition:**
   - If `word1[i-1] == word2[j-1]`, then `dp[i][j] = dp[i-1][j-1]` (no operation needed)
   - Otherwise, consider:
     - Insert: `dp[i][j-1] + 1`
     - Delete: `dp[i-1][j] + 1`
     - Replace: `dp[i-1][j-1] + 1`
   - Take the minimum of these three options.
4. **Result:**
   - The answer is `dp[len(word1)][len(word2)]`.

## Annotated Code (Canonical Solution)
```python
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # delete
                    dp[i][j - 1],    # insert
                    dp[i - 1][j - 1] # replace
                )
    return dp[m][n]
```
- The DP table is filled row by row, considering all possible operations at each step.
- The time and space complexity are both O(mn), where m and n are the lengths of the two words.

## Test Cases
- `word1 = "horse", word2 = "ros"` → Output: 3
- `word1 = "intention", word2 = "execution"` → Output: 5
- `word1 = "", word2 = "abc"` → Output: 3
- `word1 = "abc", word2 = "abc"` → Output: 0

## Common Pitfalls
- Not initializing the base cases correctly.
- Confusing the order of insert/delete operations.
- Not handling empty strings properly.

## Variations
- If only insert and delete are allowed, the problem reduces to finding the length of the longest common subsequence.
- If the cost of each operation is different, adjust the DP transitions accordingly.

## Relevant Literature
- [LeetCode #72: Edit Distance](https://leetcode.com/problems/edit-distance/)
- [Dynamic Programming for Edit Distance](https://en.wikipedia.org/wiki/Edit_distance)
- CLRS, Section 15.4: Dynamic Programming Examples 