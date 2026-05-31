class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = [[i] for i in range(n)]
        size = [[1] for _ in range(n)]
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                if size[root_a] < size[root_b]:
                    root_a , root_b = root_b, root_a
                parent[root_b] = root_a
                size[root_a] += size[root_b]
            