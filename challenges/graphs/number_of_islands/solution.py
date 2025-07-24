from collections import deque
from typing import List, Tuple


def user_num_islands(grid):
    """
    User-submitted solution for the Number of Islands problem.
    Args:
        grid (List[List[str]]): 2D grid map of '1's (land) and '0's (water).
    Returns:
        int: The number of islands in the grid.
    """
    height = len(grid)
    width = len(grid[0])
    islands = 0

    def get_neighbors(x: int, y: int) -> List[Tuple[int, int]]:
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dx, dy in deltas:
            new_x, new_y = x + dx, y + dy
            if (
                0 <= new_x < width
                and 0 <= new_y < height
                and grid[new_y][new_x] == "1"
            ):
                neighbors.append((new_x, new_y))
        return neighbors

    def sink_island(x: int, y: int):
        q = deque([(x, y)])

        # bfs to set neighboring parts of island to zero
        while q:
            nx, ny = q.popleft()
            for nnx, nny in get_neighbors(nx, ny):
                q.append((nnx, nny))
            grid[ny][nx] = "0"  # sink

    for x in range(width):
        for y in range(height):
            if grid[y][x] == "1":
                islands += 1
                sink_island(x, y)

    return islands


def canonical_num_islands(grid):
    """
    Canonical solution for the Number of Islands problem (reference
    implementation).
    Args:
        grid (List[List[str]]): 2D grid map of '1's (land) and '0's (water).
    Returns:
        int: The number of islands in the grid.
    """
    if not grid or not grid[0]:
        return 0
    height, width = len(grid), len(grid[0])
    islands = 0

    def dfs(x, y):
        if x < 0 or x >= width or y < 0 or y >= height or grid[y][x] != "1":
            return
        grid[y][x] = "0"
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

    for y in range(height):
        for x in range(width):
            if grid[y][x] == "1":
                islands += 1
                dfs(x, y)
    return islands
