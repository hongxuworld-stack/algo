from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] ==0 or  grid[r][c] ==2:
                return
            if grid[r][c] == 1:
                grid[r][c] = 2
                q.append((r,c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr,nc)
        found = False
        for r in range(rows):
            if found:
                break
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r,c)
                    found = True
                    break
        step = 0
        while len(q):
            for _ in range(len(q)):
                r , c = q.popleft()
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0<=nr<rows and 0<=nc<cols:
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            q.append((nr,nc))
                        if grid[nr][nc] == 1:
                            return step
            step +=1
        return -1

            
# Time: O(rows * cols)
# Space: O(rows * cols), for DFS recursion and the BFS queue
