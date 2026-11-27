from collections import deque
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0

        queue = deque([(0, 0)])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:

            r, c = queue.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:

                    cost = grid[nr][nc]
                    new_cost = dist[r][c] + cost

                    if new_cost < dist[nr][nc]:

                        dist[nr][nc] = new_cost

                        if cost == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))

        return dist[rows - 1][cols - 1]