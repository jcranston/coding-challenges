import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_sorted_lists(lists):
    """
    Merges k sorted linked lists into one sorted linked list.
    Args:
        lists (List[ListNode]): List of ListNode heads, each representing a
        sorted linked list.
    Returns:
        ListNode: The head of the merged sorted linked list.
    """
    k = len(lists)
    heap = []  # min heap
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
