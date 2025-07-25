# Explanation: Shortest Word Distance (LeetCode 243)

## Problem Recap
Given an array of strings `wordsDict` and two different strings `word1` and `word2`, return the shortest distance between these two words in the list. The distance is defined as the absolute difference between the indices of the two words. Both words are guaranteed to appear in the list and are not the same.

## High-Level Approach
The main idea is to scan through the list once, keeping track of the most recent indices where `word1` and `word2` were seen. Each time either word is found, update the minimum distance if both have been seen at least once. This approach ensures an efficient O(n) solution.

## Step-by-Step Breakdown
1. **Initialize:**
   - Set two variables to store the most recent indices of `word1` and `word2` (e.g., `idx1` and `idx2`), both initialized to `-1`.
   - Set `min_dist` to a large value (e.g., `float('inf')`).
2. **Iterate through the list:**
   - For each index and word in `wordsDict`:
     - If the word matches `word1`, update `idx1`.
     - If the word matches `word2`, update `idx2`.
     - If both indices are not `-1`, update `min_dist` with the absolute difference between `idx1` and `idx2` if it is smaller than the current `min_dist`.
3. **Return:**
   - After the loop, return `min_dist`.

## Annotated Canonical Solution (to be implemented)
```python
def shortest_word_distance(wordsDict, word1, word2):
    """
    Returns the shortest distance between word1 and word2 in wordsDict.
    Args:
        wordsDict: List of strings.
        word1: First target word (string).
        word2: Second target word (string).
    Returns:
        Integer representing the minimum distance between the two words.
    """
    idx1, idx2 = -1, -1
    min_dist = float('inf')
    for i, word in enumerate(wordsDict):
        if word == word1:
            idx1 = i
        elif word == word2:
            idx2 = i
        if idx1 != -1 and idx2 != -1:
            min_dist = min(min_dist, abs(idx1 - idx2))
    return min_dist
```
- **Why this works:**
  - By always updating the most recent indices, we ensure that the minimum distance is found efficiently in a single pass.
  - The approach is O(n) time and O(1) space.

## Test Cases & Edge Cases
- `wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"` → `3`
- `wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"` → `1`
- Edge: adjacent words, words at the start/end, multiple occurrences.

## Common Pitfalls
- Not updating both indices before checking the distance (can lead to using `-1` as an index).
- Forgetting to check both directions (the absolute difference handles this).
- Assuming words only appear once (they can appear multiple times).

## Variations
- If `word1` and `word2` can be the same, the logic must be adjusted to avoid comparing the same index.
- If the list is very large and queried multiple times, consider preprocessing with a map of word indices.

## Relevant Literature
- [LeetCode 243: Shortest Word Distance](https://leetcode.com/problems/shortest-word-distance/)
- [LeetCode Discuss: O(n) Solution](https://leetcode.com/problems/shortest-word-distance/solutions/67163/simple-python-solution/)

## Invariants
- At each step, `min_dist` holds the smallest distance found so far between the two words.

---
This explanation references the problem statement, canonical solution, and test cases, and follows the conventions in `ai_context/explanation_generation.md`. 