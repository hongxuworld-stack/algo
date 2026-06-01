    # 0 representing an empty cell,
    # 1 representing a fresh orange, or
    # 2 representing a rotten orange.
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh_count = 0
        q = deque()
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        while len(q) and fresh_count>0:
            level_size = len(q)
            for _ in range(level_size):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] ==1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh_count -= 1
            minutes += 1
        return minutes if fresh_count == 0 else -1
        
# return [nr][nc]
# Time: O(rows * cols)
# Space: O(rows * cols), for the BFS queue in the worst case
