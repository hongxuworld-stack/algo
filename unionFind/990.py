class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        size = [1 for _ in range(26)]
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b,root_a
            parent[root_b] = root_a
            size[root_a] += size[root_b]
        for eq in equations:
            if eq[1] == "=":
                a = ord(eq[0]) - ord("a")
                b = ord(eq[3]) - ord("a")
                union(a,b)
        for eq in equations:
            if eq[1] == "!":
                a = ord(eq[0]) - ord("a")
                b = ord(eq[3]) - ord("a")
                root_a = find(a)
                root_b = find(b)
                if root_a == root_b:
                    return False
        return True