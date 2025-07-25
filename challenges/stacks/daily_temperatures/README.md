**LeetCode #739**  
**Tags:** stack, array, monotonic stack

# Daily Temperatures

## Problem
Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

## Examples

### Example 1
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Explanation: As you can see from the first day, the temperature is 73, and the next day it is 74, so you have to wait 1 day. On the second day, the temperature is 74, and the next day it is 75, so you have to wait 1 day. On the third day, the temperature is 75, and the next day it is 71, so you have to wait 4 days to get a warmer temperature, and so on.
```

### Example 2
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

### Example 3
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

## Constraints
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

## Clarifications & Assumptions
- The array represents daily temperatures in order.
- We need to find the next warmer day for each day.
- If no warmer day exists, the answer is 0.
- The answer array has the same length as the input array.

## Approach
- Use a monotonic stack to keep track of indices of temperatures.
- For each temperature, pop from the stack all indices where the temperature is lower than the current one.
- The difference between current index and popped index gives the number of days to wait.
- Time complexity: O(n), space complexity: O(n).

## Notes
- Edge cases: all temperatures decreasing, all temperatures increasing, single element array.
- This is a classic monotonic stack problem for finding next greater element. 