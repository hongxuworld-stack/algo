import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        effort = [[float("inf")] * cols for _ in range(rows)]
        effort[0][0] = 0
        heap = [(0,0,0)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while heap:
            cur_effort, r, c = heapq.heappop()
            if r == rows-1 and c == cols -1:
                return cur_effort
            if effort[r][c] < cur_effort:
                continue
            effort[r][c] = cur_effort
            for dr, dc in  directions:
                nr = r + dr
                nc = c + dc
                if 0<=nr<rows and 0<=nc<cols:
                    diff = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(diff, cur_effort)
                    if new_effort < effort[nr][nc]:
                        heap.heappush((new_effort,nr,nc))