**LeetCode #243**  
**Tags:** array, two pointers

# Shortest Word Distance

Given an array of strings `wordsDict` and two different strings `word1` and `word2`, return the shortest distance between these two words in the list.

## Example
```
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
```

## Constraints
- 2 <= wordsDict.length <= 3 * 10^4
- 1 <= wordsDict[i].length <= 10
- wordsDict[i] consists of lowercase English letters.
- word1 and word2 are in wordsDict.
- word1 != word2

## Clarifications & Assumptions
- The distance is the absolute difference between the indices of the two words.
- The function should return the minimum such distance for all pairs in the list.

## Approach
- Use a single pass through the list, tracking the most recent indices of `word1` and `word2`.
- Update the minimum distance whenever both have been seen.

## Notes
- Edge cases: adjacent words, words at the start/end, multiple occurrences.
- Time complexity: O(n), where n is the length of wordsDict.
- Space complexity: O(1). 