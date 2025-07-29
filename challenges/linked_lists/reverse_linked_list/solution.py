from typing import Optional


class ListNode:
    """Node for singly linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverses a singly linked list.

    Args:
        head: The head node of the singly linked list.

    Returns:
        The new head node of the reversed linked list, or None if the list is
        empty.
    """
    prev = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev
