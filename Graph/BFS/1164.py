#1 represents land
from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dist = [[-1] * cols for _ in range(rows)]
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r,c))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if not q or len(q) == rows * cols:
            return -1
        while len(q):
            r,c = q.popleft()
            for dr, dc in directions:
                nr = r + dr 
                nc = c + dc
                if  0<=nr<rows and 0<=nc<cols and dist[nr][nc] == -1:
                     dist[nr][nc] =  dist[r][c] + 1
                     q.append((nr,nc))
        max_val = -1
        for r in range(rows):
            for c in range(cols):
                max_val = max(max_val,dist[r][c])
        return max_val
