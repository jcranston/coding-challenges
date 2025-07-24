# Explanation: Check if the Sentence Is Pangram (LeetCode 1832)

## Problem Recap
A pangram is a sentence where every letter of the English alphabet appears at least once. Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

## Approach
- Use a set to track all unique letters seen in the sentence.
- Iterate through each character in the sentence and add it to the set.
- After processing, check if the set contains all 26 lowercase English letters.
- If so, return True; otherwise, return False.

## Code Reasoning
- Sets are ideal for tracking unique elements.
- The check `len(seen) == 26` ensures all letters are present.
- This approach is O(n) time and O(1) space (since the alphabet size is constant).

## Edge Cases
- Sentence shorter than 26 characters: cannot be a pangram.
- Sentence with repeated letters: still valid as long as all 26 are present.
- Empty string: returns False.

## Why Use a Set?
- Efficiently tracks unique letters.
- Avoids unnecessary counting or sorting.

## Related Literature
- Pangram problems are common in string manipulation and set usage.
- See [Wikipedia: Pangram](https://en.wikipedia.org/wiki/Pangram) and [LeetCode Discuss](https://leetcode.com/problems/check-if-the-sentence-is-pangram/solutions/1090082/python-3-set-solution/).

## Invariants
- The set always contains the unique letters seen so far.
- The function returns as soon as all 26 letters are found (optional optimization).

## Code Example
```python
def check_if_pangram(sentence):
    return len(set(sentence)) == 26
``` 