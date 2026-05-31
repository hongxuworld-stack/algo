# 305. Number of Islands II
# You are given an empty 2D grid of size m x n.
# Initially, all cells are water.
# You are also given an array positions, where positions[i] = [row, col].
# Each position represents adding land to the grid at that cell.
# After each land addition, return the number of islands in the grid.
# An island is formed by connecting adjacent lands horizontally or vertically.
# Diagonal connections do not count.
# Return an array answer, where answer[i] is the number of islands after the i-th land addition.
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = [-1 for _ in range(m*n)]
        size = [1 for _ in range(m*n)]
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
        def weighed_position(r,c):
            return r*n + c
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        num_island = 0
        res = []
        for r,c in positions:
            p = weighed_position(r,c)
            if parent[p] != -1:
                res.append(num_island)
                continue
            num_island += 1
            parent[p] = p
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if 0<=nr<=m-1 and 0<=nc<=n-1:
                    np = weighed_position(nr,nc)
                    if parent[np] != -1:
                        if union(p,np):
                            num_island -= 1
            res.append(num_island)
        return res