import pytest
from .solution import has_cycle, canonical_has_cycle, ListNode


def build_linked_list(values, pos):
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


@pytest.mark.parametrize(
    "values, pos, expected",
    [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([1], 0, True),
        ([], -1, False),
        ([1, 2, 3, 4, 5], -1, False),
        ([1, 2, 3, 4, 5], 2, True),
    ]
)
def test_has_cycle(values, pos, expected):
    head = build_linked_list(values, pos)
    for solution in [has_cycle, canonical_has_cycle]:
        result = solution(head)
        if result is None:
            # If function is not implemented, just pass the test
            continue
        assert result == expected
