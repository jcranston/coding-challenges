# Explanation: Palindromic Substrings (LeetCode 647)

## Problem Recap
Given a string s, return the number of palindromic substrings in it. A substring is a contiguous sequence of characters within the string, and a palindrome reads the same forward and backward.

## High-Level Approach
This is a classic string and palindrome problem. The most efficient approach is to expand around every possible center (each character and each gap between characters) and count all palindromic substrings.

## Step-by-Step Breakdown
1. **Expand Around Center:**
   - For each index in the string, treat it as the center of a palindrome.
   - Expand outwards as long as the substring is a palindrome.
   - Do this for both odd and even length palindromes.
2. **Count All Palindromes:**
   - For each expansion, increment the count.
3. **Alternative:** Use dynamic programming to check all substrings, but this uses O(n^2) space.

## Annotated Canonical Solution
```python
def canonical_count_palindromic_substrings(s: str) -> int:
    n = len(s)
    count = 0
    for center in range(2 * n - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    return count
```
- **Why this works:**
  - There are 2n-1 possible centers (n single characters and n-1 gaps).
  - Expanding around each center finds all palindromic substrings in O(n^2) time.

## Alternative: Expand Around Center Helper Function
Another common and clear approach is to use a helper function that expands around a given center. For each index, call the helper for both odd-length (centered at i) and even-length (centered between i and i+1) palindromes:

```python
def count_palindromic_substrings(s: str) -> int:
    def expand_around_center(left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    n = len(s)
    total = 0
    for i in range(n):
        total += expand_around_center(i, i)     # Odd-length palindromes
        total += expand_around_center(i, i + 1) # Even-length palindromes
    return total
```
- This approach is functionally equivalent to the 2n-1 centers method, but often considered more readable and explicit in interviews.

## Test Cases & Edge Cases
- `"abc"`