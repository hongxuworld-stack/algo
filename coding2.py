from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            start = equations[i][0]
            end = equations[i][1]
            value = values[i]
            graph[start].append((end, value))
            graph[end].append((start, 1 / value))

        visited = set()
        weight_mapping = {}
        root_mapping = {}

        def dfs(node, cur_ratio, root):
            if node in visited:
                return

            weight_mapping[node] = cur_ratio
            root_mapping[node] = root
            visited.add(node)

            for nei, value in graph[node]:
                dfs(nei, cur_ratio / value, root)

        for node in graph:
            dfs(node, 1, node)

        res = []
        for i in range(len(queries)):
            start = queries[i][0]
            end = queries[i][1]

            if start not in graph or end not in graph:
                res.append(-1.0)
                continue

            root_start = root_mapping[start]
            root_end = root_mapping[end]
            if root_start != root_end:
                res.append(-1.0)
            else:
                res.append(weight_mapping[start] / weight_mapping[end])
        return res
