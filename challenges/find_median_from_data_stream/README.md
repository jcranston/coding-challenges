# Find Median from Data Stream

## Problem
The MedianFinder class is designed to efficiently add numbers from a data stream and find the median of all elements so far.

Implement the MedianFinder class:
- `MedianFinder()` initializes the object.
- `add_num(num)` adds the integer num from the data stream to the data structure.
- `find_median()` returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.

## Example
```
Input:
["MedianFinder", "add_num", "add_num", "find_median", "add_num", "find_median"]
[[], [1], [2], [], [3], []]
Output:
[null, null, null, 1.5, null, 2.0]
Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.add_num(1);    // arr = [1]
medianFinder.add_num(2);    // arr = [1, 2]
medianFinder.find_median(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.add_num(3);    // arr = [1, 2, 3]
medianFinder.find_median(); // return 2.0
```

## Constraints
- -10^5 <= num <= 10^5
- There will be at least one element before calling find_median.
- At most 5 * 10^4 calls will be made to add_num and find_median.

## Clarifications & Assumptions
- The data structure must support efficient insertion and median finding.
- The median is the middle value if the number of elements is odd, or the average of the two middle values if even.
- The input stream may be in any order.

## Approach
Describe your approach and thought process after attempting the problem. Consider using two heaps for optimal performance.

## Notes
- Edge cases: all numbers the same, negative numbers, large number of elements, calling find_median before any add_num (should not happen per constraints). 