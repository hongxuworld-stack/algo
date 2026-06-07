import heapq

class Solution:
    # def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
    #     heap = []
    #     for i in range(len(heights) - 1):
    #         diff = heights[i + 1] - heights[i]
    #         if diff <= 0:
    #             continue
    #         if ladders > 0:
    #             heapq.heappush(heap, diff)
    #             ladders -= 1
    #         else:
    #             if heap and heap[0] < diff:
    #                 # ladder 给当前更大的 diff
    #                 smallest_ladder_diff = heapq.heappop(heap)
    #                 bricks -= smallest_ladder_diff
    #                 heapq.heappush(heap, diff)
    #             else:
    #                 # 当前 diff 比 ladder 里的都小，直接用 bricks
    #                 bricks -= diff

    #             if bricks < 0:
    #                 return i

    #     return len(heights) - 1

def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
    heap = []
    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff <= 0:
            continue
        heapq.heappush(heap,diff)
        if len(heap) > ladders:
            bricks -= heapq.heappop(heap)
        if bricks < 0:
            return i
    return len(heights) - 1