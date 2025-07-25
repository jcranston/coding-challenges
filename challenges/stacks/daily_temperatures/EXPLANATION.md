# Explanation: Daily Temperatures (LeetCode 739)

## Problem Recap
Given an array of integers `temperatures` representing daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0`.

## High-Level Approach
This is a classic monotonic stack problem. The key insight is to use a stack to keep track of indices of temperatures that are waiting for a warmer day. For each temperature, we pop from the stack all indices where the temperature is lower than the current one, as those days have found their warmer temperature.

## Step-by-Step Breakdown
1. **Initialize:**
   - Create an empty stack to store indices.
   - Create an answer array initialized with zeros.
2. **Iterate through temperatures:**
   - For each temperature, while the stack is not empty and the current temperature is greater than the temperature at the top of the stack:
     - Pop the index from the stack.
     - Calculate the difference between current index and popped index.
     - Set `answer[popped_index] = current_index - popped_index`.
   - Push the current index onto the stack.
3. **Result:**
   - The answer array contains the number of days to wait for each day.

## Annotated Canonical Solution
```python
from typing import List

def canonical_daily_temperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    answer = [0] * n
    stack = []
    
    for i in range(n):
        # Pop all indices where the temperature is lower than current
        while stack and temperatures[stack[-1]] < temperatures[i]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        stack.append(i)
    
    return answer
```
- **Why this works:**
  - The stack maintains a monotonic decreasing sequence of temperatures.
  - When we encounter a warmer temperature, we resolve all the waiting days.
  - The stack ensures we process temperatures in the correct order.

## Test Cases & Edge Cases
- `[73,74,75,71,69,72,76,73]` → `[1,1,4,2,1,1,0,0]`
- `[30,40,50,60]` → `[1,1,1,0]`
- `[30,60,90]` → `[1,1,0]`
- `[30]` → `[0]` (single element)
- `[30,30,30]` → `[0,0,0]` (all same temperature)
- `[90,80,70,60]` → `[0,0,0,0]` (decreasing temperatures)
- `[60,70,80,90]` → `[1,1,1,0]` (increasing temperatures)

## Common Pitfalls
- Not handling the case where no warmer day exists (stack remains non-empty).
- Forgetting to push the current index onto the stack after processing.
- Not understanding that the stack maintains a monotonic decreasing sequence.

## Variations
- **Next Greater Element:** Find the next greater element for each element in an array.
- **Next Smaller Element:** Find the next smaller element (use increasing stack).
- **Previous Greater Element:** Process the array in reverse order.

## Relevant Literature
- [LeetCode 739: Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
- [Monotonic Stack - GeeksforGeeks](https://www.geeksforgeeks.org/monotonic-stack/)
- [Next Greater Element - CLRS, Chapter 10](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)

---
This explanation references the problem statement, canonical solution, and test cases, and follows the conventions in `ai_context/explanation_generation.md`. 