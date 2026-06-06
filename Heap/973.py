import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = point[0] ** 2 + point[1] **2
            heapq.heappush(heap,(dist,point))
        res = []
        for _ in range(k):
            dist, point = heapq.heappop(heap)
            res.append(point)
        return res