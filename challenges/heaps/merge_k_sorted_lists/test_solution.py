from .solution import ListNode, merge_k_sorted_lists


def list_to_nodes(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def nodes_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def test_merge_k_sorted_lists():
    lists = [
        list_to_nodes([1, 4, 5]),
        list_to_nodes([1, 3, 4]),
        list_to_nodes([2, 6]),
    ]
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    result = merge_k_sorted_lists(lists)
    assert nodes_to_list(result) == expected

    lists = []
    expected = []
    result = merge_k_sorted_lists(lists)
    assert nodes_to_list(result) == expected

    lists = [list_to_nodes([]), list_to_nodes([])]
    expected = []
    result = merge_k_sorted_lists(lists)
    assert nodes_to_list(result) == expected
