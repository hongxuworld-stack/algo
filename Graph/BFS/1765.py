from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])
        q = deque()
        height = [[-1] * cols for i in range(rows)] 
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    height[r][c] = 0
                    q.append((r,c))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while len(q):
            r,c = q.popleft()
            for dr, dc in directions:
                nr = r + dr 
                nc = c + dc
                if 0<=nr<rows and 0<=nc<cols and height[nr][nc] == -1:
                    height[nr][nc] = height[r][c] + 1
                    q.append((nr,nc))
        return height
