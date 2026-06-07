import heapq
from collections import defaultdict
from typing import List
class Solution:
    # def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    #     graph = defaultdict(list)
    #     for u,v,w in times:
    #         graph[u].append((w,v))
    #     heap = [(0,k)]
    #     distances = [float("inf")] * (n + 1)
    #     while heap:
    #         cur_dis, node = heapq.heappop(heap)
    #         # if node in distances:
    #         if distances[node] != float("inf"):
    #             continue
    #         distances[node] = cur_dis
    #         for w,v in graph[node]:
    #             if distances[v] == float("inf"):
    #                 new_dist = w + cur_dis
    #                 heapq.heappush(heap, (new_dist, v))
    #     ans = max(dist_list[1:])
    #     return ans if ans != float("inf") else -1


    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w,v))
        dist_list = [float("inf")] * (n + 1)
        heap = [(0,k)]
        while heap:
            dist , node = heapq.heappop(heap)
            if dist > dist_list[node]:
                continue
            for weight, neighbor in graph[node]:
                new_dist = weight + dist
                if new_dist < dist_list[neighbor]:
                    dist_list[neighbor] = new_dist
                    heapq.heappush(heap,(new_dist,neighbor))
        ans = max(dist_list[1:])
        return ans if ans != float("inf") else -1

