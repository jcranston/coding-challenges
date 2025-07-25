# Explanation: Merge k Sorted Lists

## Problem Recap
Given an array of `k` linked lists, each sorted in ascending order, merge all the linked lists into one sorted linked list and return it.

## High-level Approach
A brute-force approach would concatenate all lists and sort the result, but this is inefficient. The optimal solution uses a **min-heap (priority queue)** to efficiently merge the lists in O(N log k) time, where N is the total number of nodes and k is the number of lists.

## Step-by-step Breakdown
1. **Initialize the Heap:**
   - For each non-empty list, push its head node (value, list index, node) into the min-heap.
   - The heap always contains at most k elements (one from each list).
2. **Merge Process:**
   - Pop the smallest element from the heap (the node with the smallest value).
   - Add this node to the merged list.
   - If the popped node has a next node, push it into the heap.
   - Repeat until the heap is empty.
3. **Result:**
   - The merged list is built by always choosing the smallest available node from the heap.

## Annotated Code
```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists):
    k = len(lists)
    heap = []
    for i in range(k):
        if lists[i]:
            head = lists[i]
            heapq.heappush(heap, (head.val, i, head))
    head = ListNode(0)
    current = head
    while heap:
        val, list_idx, node = heapq.heappop(heap)
        current.next = ListNode(val)
        current = current.next
        next_node = node.next
        if node.next:
            heapq.heappush(heap, (next_node.val, list_idx, next_node))
    return head.next
```
- The heap ensures that the smallest node among all current list heads is always chosen next.
- Time complexity is O(N log k), where N is the total number of nodes and k is the number of lists.

## Test Cases
- `lists = [[1,4,5],[1,3,4],[2,6]]` → Output: `[1,1,2,3,4,4,5,6]`
- `lists = []` → Output: `[]`
- `lists = [[], []]` → Output: `[]`

## Common Pitfalls
- Not handling empty lists or lists with different lengths.
- Not pushing the next node of a list into the heap after popping its current node.
- Creating cycles in the merged list by reusing nodes (always create new nodes for the merged list).

## Variations
- If the lists are arrays instead of linked lists, use array indices in the heap.
- If you want to merge in place, adjust the node pointers instead of creating new nodes.

## Relevant Literature
- [LeetCode #23: Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [Heap (Priority Queue) Data Structure](https://en.wikipedia.org/wiki/Heap_(data_structure))
- CLRS, Section 6.5: Priority Queues 