from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = {}
        size = {}
        weight = {}
        def add(x):
            if x not in parent:
                parent[x] = x
                size[x] = 1
                weight[x] = 1
        def find(x):
            add(x)
            if x != parent[x]:
                ori_parent = parent[x]
                parent[x] = find(parent[x])
                weight[x]  *= weight[ori_parent]
            return parent[x]
        def union(a,b,val):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return

            if size[root_a] < size[root_b]:
                a, b = b, a
                root_a, root_b = root_b, root_a
                val = 1 / val

            parent[root_b] = root_a
            weight[root_b] = weight[a] / (val * weight[b])
            size[root_a] += size[root_b]
        
        for i in range(len(equations)):
            start = equations[i][0]
            end = equations[i][1]
            value = values[i]
            union(start, end, value)

        res = []
        for i in range(len(queries)):
            start = queries[i][0]
            end = queries[i][1]

            if start not in parent or end not in parent:
                res.append(-1.0)
                continue

            root_start = find(start)
            root_end = find(end)
            if root_start != root_end:
                res.append(-1.0)
            else:
                res.append(weight[start] / weight[end])
        return res

    def calcEquationDFS(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (start, end), value in zip(equations, values):
            graph[start].append((end, value))
            graph[end].append((start, 1 / value))

        visited = set()
        weight_mapping = {}
        root_mapping = {}

        def dfs(node, cur_ratio, root):
            if node in visited:
                return

            visited.add(node)
            weight_mapping[node] = cur_ratio
            root_mapping[node] = root

            for nei, value in graph[node]:
                dfs(nei, cur_ratio / value, root)

        for node in graph:
            dfs(node, 1, node)

        res = []
        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1.0)
                continue

            if root_mapping[start] != root_mapping[end]:
                res.append(-1.0)
            else:
                res.append(weight_mapping[start] / weight_mapping[end])

        return res
            
