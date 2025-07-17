from typing import Optional

from .solution import ListNode, reverse_linked_list


def as_list(head: Optional[ListNode]):
    result = []
    cur = head
    while cur is not None:
        result.append(cur.val)
        cur = cur.next
    return result


def test_example():
    n3 = ListNode(3, None)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    assert as_list(reverse_linked_list(n1)) == [3, 2, 1]


def test_one_element():
    n = ListNode(1, None)
    assert as_list(reverse_linked_list(n)) == [1]


def test_two_elements():
    n2 = ListNode(2, None)
    n1 = ListNode(1, n2)
    assert as_list(reverse_linked_list(n1)) == [2, 1]


def test_no_elements():
    n = None
    assert as_list(reverse_linked_list(n)) == []
