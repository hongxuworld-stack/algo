import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        efforts = [[float("inf")] * cols for _ in range(rows)]
        efforts[0][0] = 0
        heap = [(0,0,0)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while(heap):
            cur_effort,r,c = heapq.heappop(heap)
            if r == rows - 1 and c == cols - 1:
                return cur_effort
            if efforts[r][c] < cur_effort:
                continue
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0<=nr<rows and 0<=nc<cols:
                    diff = abs(heights[nr][nc] - heights[r][c])
                    new_effort = max(cur_effort, diff)
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(heap,(new_effort,nr,nc))
        return 0