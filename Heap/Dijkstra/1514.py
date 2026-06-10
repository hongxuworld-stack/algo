from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            edge = edges[i]
            start = edge[0]
            end = edge[1]
            prob = succProb[i]
            graph[start].append((prob,end))
            graph[end].append((prob,start))
        probs_list = [0 for _ in range(n)]
        probs_list[start_node] = 1
        heap = [(-1,start_node)]
        while heap:
            cur_prob, node = heapq.heappop(heap)
            cur_prob = -cur_prob
            if cur_prob < probs_list[node]:
                continue
            for prob,nei in graph[node]:
                new_prob = cur_prob * prob
                if new_prob > probs_list[nei]:
                    probs_list[nei] = new_prob
                    heapq.heappush(heap, (-new_prob,nei))
        return probs_list[end_node]