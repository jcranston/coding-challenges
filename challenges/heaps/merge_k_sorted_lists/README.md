**LeetCode #23**  
**Tags:** linked list, heap, divide and conquer, merge

# Merge k Sorted Lists

## Problem
You are given an array of `k` linked lists, each linked list is sorted in ascending order. Merge all the linked lists into one sorted linked list and return it.

## Example
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked lists are:
[1->4->5], [1->3->4], [2->6]
Merging them into one sorted list: 1->1->2->3->4->4->5->6
```

## Constraints
- k == len(lists)
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The total number of nodes across all lists is <= 10^4

## Clarifications & Assumptions
- If all input lists are empty, return an empty list.
- The returned list should be a new linked list, not modify the input lists.
- You may use a min-heap for optimal performance.

## Approach
Describe your approach and thought process after attempting the problem. Consider using a heap for optimal performance.

## Notes
- Edge cases: all lists empty, some lists empty, lists of different lengths, duplicate values, negative numbers. 