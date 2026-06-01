class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c):
            if r<0 or r>= rows or c<0 or c>= cols:
                return
            if grid[r][c] == 1:
                grid[r][c] = 0
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    dfs(nr,nc)
        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)
        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==1:
                    res += 1
        return res

# Time: O(rows * cols)
# Space: O(rows * cols), for DFS recursion in the worst case
