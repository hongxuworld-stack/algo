from collections import defaultdict
from typing import List, Dict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        size = [1  for _ in range(n)]
        def find(x):
            if x != parent[x]:
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
        email_map = {}
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email in email_map:
                    union(i,email_map[email])
                email_map[email] = i
        res_map = defaultdict(set)
        for i,account in enumerate(accounts):
            root = find(i)
            for email in account[1:]:
                res_map[root].add(email)
        res  = []
        for root, emails in res_map.items():
            name = accounts[root][0]
            res.append([name] + sorted(emails))
        return res

