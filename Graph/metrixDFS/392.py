class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        dp = [[0] * cols for _ in range(rows)]
        def dfs(r,c):
            if dp[r][c] != 0:
                return dp[r][c]
            best = 1
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr>=0 and nr<rows and nc>=0 and nc<cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best,dfs(nr,nc) + 1)
            dp[r][c] = best
            return best
        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res,dfs(r,c))
        return res
    
# boundary check can  be moved after visited check(no need to be always top)
# Time: O(rows * cols), each cell's dfs result is memoized once
# Space: O(rows * cols), for dp and recursion stack
