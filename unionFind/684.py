class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        size = [1 for i in range(n+1)]
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return False
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            parent[root_b] = root_a
            size[root_a] += size[root_b]
            return True
        for start,end in edges:
            if not union(start,end):
                return[start,end]
        return None

# Time: O(n * alpha(n)), where n = len(edges)
# Space: O(n)
#Time complexity is O(n α(n)), which is almost O(n) in practice. Space complexity is O(n) because we maintain the parent and size arrays.
