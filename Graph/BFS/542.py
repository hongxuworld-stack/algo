from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        q = deque()
        dist = [[-1]* cols for _ in range(rows)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r,c))
        while len(q):
            r,c = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0<=nr<rows and 0<=nc<cols and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr,nc))
        return dist
