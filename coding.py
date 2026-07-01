# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# a ->(2) b -> c (3)
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            start = equations[i][0]
            end = equations[i][1]
            value = values[i]
            graph[start].append((end,value))
            graph[end].append((start,1/value))
        res = []
        for i in range(len(queries)):
            start = queries[i][0]
            end = queries[i][1]
            if start not in graph or end not in graph:
                res.append(-1.0)
                continue
            if start == end:
                res.append(1)
                continue
            visited = set()
            ration = 1
            node_find = False
            def dfs(node,cur_ration,target):
                nonlocal ration
                nonlocal node_find
                if node_find:
                    return
                if  node in visited:
                    return cur_ration
                if node == target:
                    node_find = True
                    ration = cur_ration
                visited.add(node)
                for nei, value in graph[node]:
                    dfs(nei,cur_ration * value, target)
                return cur_ration
            dfs(start,ration,end)
            if node_find:
                res.append(ration)
            else:
                res.append(-1.0)
        return res