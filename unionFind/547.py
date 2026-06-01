class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        def find(x):
            if  x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parent[root_a] = root_b
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] ==1:
                    union(i,j)
        res = set()
        for i in range(n):
            res.add(find(i))
        return len(res)

# Time: O(n^2 * alpha(n)), because we scan the upper triangle of the matrix
# Space: O(n)
