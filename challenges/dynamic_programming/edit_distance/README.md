**LeetCode #72**  
**Tags:** dynamic programming, string

# Edit Distance

## Problem
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You may perform the following operations on a word:
- Insert a character
- Delete a character
- Replace a character

## Examples
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
 horse -> rorse (replace 'h' with 'r')
 rorse -> rose (remove 'r')
 rose -> ros (remove 'e')

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
 intention -> inention (remove 't')
 inention -> enention (replace 'i' with 'e')
 enention -> exention (replace 'n' with 'x')
 exention -> exection (replace 'n' with 'c')
 exection -> execution (insert 'u')
```

## Constraints
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters.

## Clarifications & Assumptions
- The minimum number of operations is the edit distance between the two words.
- You may use dynamic programming for optimal performance.

## Approach Hints
- Consider using a 2D DP table where dp[i][j] represents the edit distance between the first i characters of word1 and the first j characters of word2.
- Think about the three possible operations at each step. 