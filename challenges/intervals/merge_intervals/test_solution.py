from .solution import merge_intervals, merge_intervals_deque

solutions = [merge_intervals, merge_intervals_deque]


def test_merge_intervals_example():
    assert all(
        solve([[1, 3], [2, 6], [8, 10], [15, 18]])
        == [[1, 6], [8, 10], [15, 18]]
        and solve([[1, 4], [4, 5]]) == [[1, 5]]
        for solve in solutions
    )


def test_merge_intervals_edge_cases():
    assert all(
        solve([]) == []
        and solve([[1, 2]]) == [[1, 2]]
        and solve([[1, 4], [0, 2], [3, 5]]) == [[0, 5]]
        and solve([[1, 4], [0, 4]]) == [[0, 4]]
        and solve([[1, 4], [2, 3]]) == [[1, 4]]
        for solve in solutions
    )
