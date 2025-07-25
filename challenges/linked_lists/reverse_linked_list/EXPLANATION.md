# Reverse Linked List — EXPLANATION

## Problem Recap
Given the head of a singly linked list, reverse the list, and return the head of the reversed list.

## High-Level Approach
Iteratively traverse the list, reversing the direction of each node's `next` pointer as you go. Alternatively, use recursion.

## Step-by-Step Solution (Iterative)
1. Initialize `prev` to `None` and `cur` to the head of the list.
2. While `cur` is not `None`:
    - Store `cur.next` in a temporary variable.
    - Set `cur.next` to `prev` (reverse the pointer).
    - Move `prev` to `cur` and `cur` to the next node.
3. When done, `prev` will be the new head of the reversed list.

## Annotated Code
```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev
```

## Example Test Cases
```python
# Helper to build and print linked lists for testing

def build_list(vals):
    head = ListNode(vals[0]) if vals else None
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def to_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals

head = build_list([1,2,3,4,5])
reversed_head = reverse_linked_list(head)
assert to_list(reversed_head) == [5,4,3,2,1]
```

## Common Pitfalls
- Not updating all pointers (can lose part of the list).
- Not handling empty lists (should return `None`).
- Accidentally creating cycles in the list.

## Variations
- Reverse a sublist between two positions.
- Reverse the list recursively.

## References
- [LeetCode #206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [Linked List Patterns](https://leetcode.com/problems/reverse-linked-list/solutions/) 