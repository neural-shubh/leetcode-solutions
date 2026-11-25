
from typing import List
from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        directions = [
            (1, 0),   
            (-1, 0),  
            (0, 1),   
            (0, -1)   
        ]

        @lru_cache(None)
        def dfs(r, c):

            longest = 1

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:

                    if matrix[nr][nc] > matrix[r][c]:

                        path = 1 + dfs(nr, nc)

                        longest = max(longest, path)

            return longest

        result = 0

        for r in range(rows):
            for c in range(cols):
                result = max(result, dfs(r, c))

        return result
