def can_finish_courses_dfs(numCourses, prerequisites):
    """Canonical solution for the Course Schedule problem (reference
    implementation) using DFS.

    Args:
        numCourses (int): Total number of courses.
        prerequisites (List[List[int]]): List of prerequisite pairs [a, b].
    Returns:
        bool: True if all courses can be finished, otherwise False.
    """
    from collections import defaultdict

    graph = defaultdict(list)
    for dest, src in prerequisites:
        graph[src].append(dest)

    visited = set()
    on_path = set()

    def has_cycle(course):
        if course in on_path:
            return True
        if course in visited:
            return False
        on_path.add(course)
        for neighbor in graph[course]:
            if has_cycle(neighbor):
                return True
        on_path.remove(course)
        visited.add(course)
        return False

    for course in range(numCourses):
        if has_cycle(course):
            return False
    return True


def can_finish_courses_bfs(numCourses, prerequisites):
    """BFS (Kahn's algorithm) solution for the Course Schedule problem.

    Args:
        numCourses (int): Total number of courses.
        prerequisites (List[List[int]]): List of prerequisite pairs [a, b].
    Returns:
        bool: True if all courses can be finished, otherwise False.
    """
    from collections import defaultdict, deque

    graph = defaultdict(list)
    in_degree = [0] * numCourses
    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1

    # Start with all courses that have no prerequisites
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    finished_courses = 0

    while queue:
        course = queue.popleft()
        finished_courses += 1
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return finished_courses == numCourses
