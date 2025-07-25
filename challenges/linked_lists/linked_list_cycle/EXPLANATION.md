# Explanation: Linked List Cycle (LeetCode 141)

## Problem Recap
Given the head of a singly linked list, determine if the list contains a cycle. A cycle exists if a node can be reached again by continuously following the next pointer.

## High-Level Approach
This is a classic cycle detection problem. The most efficient solution uses two pointers (slow and fast) to traverse the list at different speeds. If there is a cycle, the fast pointer will eventually meet the slow pointer.

## Step-by-Step Breakdown
1. **Initialize two pointers:**
   - Slow pointer moves one step at a time.
   - Fast pointer moves two steps at a time.
2. **Traverse the list:**
   - If the fast pointer or its next is null, there is no cycle.
   - If slow and fast pointers meet, a cycle exists.
3. **Return the result:**
   - Return True if a cycle is detected, otherwise False.

## Annotated Canonical Solution
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def canonical_has_cycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
- **Why this works:**
  - If there is a cycle, the fast pointer will lap the slow pointer and they will meet.
  - If there is no cycle, the fast pointer will reach the end of the list.

## Test Cases & Edge Cases
- `[3,2,0,-4], pos=1` → `True` (cycle at node 1)
- `[1,2], pos=0` → `True` (cycle at head)
- `[1], pos=-1` → `False` (single node, no cycle)
- `[1], pos=0` → `True` (single node, cycle to itself)
- `[], pos=-1` → `False` (empty list)
- `[1,2,3,4,5], pos=-1` → `False` (no cycle)
- `[1,2,3,4,5], pos=2` → `True` (cycle at node 2)

## Common Pitfalls
- Not handling empty lists or single-node lists.
- Forgetting to check if fast and fast.next are not null before advancing.
- Confusing the cycle detection logic (meeting point).

## Variations
- **Find the node where the cycle begins:** LeetCode 142 (Linked List Cycle II).
- **Detect cycles in doubly linked lists or graphs.**

## Relevant Literature
- [LeetCode 141: Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [Floyd’s Tortoise and Hare Algorithm](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare)
- [CLRS, Chapter 22: Elementary Data Structures](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)

---
This explanation references the problem statement, canonical solution, and test cases, and follows the conventions in `ai_context/explanation_generation.md`. 