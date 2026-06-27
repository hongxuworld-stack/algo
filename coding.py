from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        node_mapping = {node:Node(node.val)}
        q = deque()
        q.append(node)
        while len(q):
            item = q.popleft()
            for nei in item.neighbors:
                if nei not in node_mapping:
                    node_mapping[nei] = Node(nei.val)
                    q.append(nei)
                node_mapping[item].append(node_mapping[nei])
        return node_mapping[node]
            