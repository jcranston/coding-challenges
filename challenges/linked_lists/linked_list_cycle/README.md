**LeetCode #141**  
**Tags:** linked list, two pointers, cycle detection

# Linked List Cycle

## Problem
Given the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

## Examples

### Example 1
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

### Example 2
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

### Example 3
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

## Constraints
- The number of nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked list.

## Clarifications & Assumptions
- The input is a singly linked list.
- The function should return a boolean indicating if a cycle exists.
- The cycle, if present, can be at any position in the list.

## Approach
- Use two pointers (slow and fast). Move slow by one step and fast by two steps.
- If there is a cycle, the fast pointer will eventually meet the slow pointer.
- If fast reaches the end (null), there is no cycle.
- Time complexity: O(n), space complexity: O(1).

## Notes
- Edge cases: empty list, single node with/without cycle, cycle at head or tail.
- This is a classic interview problem for cycle detection in linked lists. 