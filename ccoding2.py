from collections import defaultdict
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
                union(start,end,value)
        res = []
        for i in range(len(queries)):
            start = queries[i][0]
            end = queries[i][1]
            root_start = find(start)
            root_end=find(end)
            if not root_start or not root_end:
                res.append(-1.0)
            else:
                res.append(weight[start]/weight[end])
        return res
            