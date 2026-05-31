#support you have a list of transaction.[{t_id:"xxx","email":"xxxx","device_name":"xxxx"}]
# if t_id share same email or device_name, link them. return list of transactions.[[t_id1,t_id2],[t_id3]]
from collections import defaultdict
from typing import List, Dict
def group_transactions(transactions: List[Dict[str, str]]) -> List[List[str]]:
    n = len(transactions)
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
    attr_list = ["email","device"]
    attr_to_index = defaultdict(dict)
    for i,tx in enumerate(transactions):
        for attr in attr_list:
            value = tx.get(attr)
            if value is None:
                continue
            if value in attr_to_index[attr]:
                union(i,attr_to_index[attr][value])
            else:
                attr_to_index[attr][value] = i

    groups = defaultdict(list)
    for i, tx in enumerate(transactions):
        root = find(i)
        groups[root].append(tx["t_id"])

    return list(groups.values())

