# Given n nodes labeled from 0 to n - 1, and a list of undirected edges:

# edges[i] = [a, b]

# where a and b are connected by an undirected edge.

# Return True if these edges form a valid tree, otherwise return False.

# A valid tree means:

# 1. All nodes are connected.
# 2. There is no cycle.
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return False
            parent[root_a] = root_b
            return True
        if len(edges) != n - 1:
            return False
        for start,end in edges:
            if not union(start,end):
                return False
        return True

# Time: O(E * alpha(n)), where E = len(edges)
# Space: O(n)
