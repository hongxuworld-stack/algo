from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = [i for i in range(len(s))]
        size = [1 for _ in range(len(s))]
        def find(x):
            if x!= parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                if size[root_a] < size[root_b]:
                    root_a,root_b = root_b,root_a
                parent[root_b] = root_a
                size[root_a] += size[root_b]
        for p1,p2 in pairs:
            union(p1,p2)
        cluster_map = defaultdict(list)
        for i in range(len(s)):
            root = find(i)
            cluster_map[root].append(i)
        # cluster_list = cluster_map.values()
        # res = ["" for _ in range(len(s))]
        # for cluster in cluster_list:
        #     tmp = []
        #     for p in cluster:
        #         tmp.append(s[p])
        #     tmp.sort()
        #     for i,p in enumerate(cluster):
        #         res[p] = tmp[i]
        res = [""] * len(s)
        for cluster in cluster_map.values():
            chars = sorted(s[p] for p in cluster)
            for p, ch in zip(cluster, chars):
                res[p] = ch

        return "".join(res)