from .solution import can_finish_courses_bfs, can_finish_courses_dfs

test_cases = [
    # Example 1: Can finish
    (2, [[1, 0]], True),
    # Example 2: Cycle, cannot finish
    (2, [[1, 0], [0, 1]], False),
    # No prerequisites
    (3, [], True),
    # Multiple independent courses
    (4, [[1, 0], [2, 3]], True),
    # Larger cycle
    (3, [[0, 1], [1, 2], [2, 0]], False),
]


def test_can_finish_courses():
    for numCourses, prerequisites, expected in test_cases:
        for solution in [can_finish_courses_dfs, can_finish_courses_bfs]:
            assert solution(numCourses, prerequisites) == expected
