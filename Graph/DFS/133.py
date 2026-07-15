from typing import Optional
from collections import deque


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        node_mapping = {}

        def dfs(node):
            if node in node_mapping:
                return node_mapping[node]

            copy_node = Node(node.val)
            node_mapping[node] = copy_node

            for neighbor in node.neighbors:
                copy_node.neighbors.append(dfs(neighbor))

            return copy_node

        return dfs(node)

    def cloneGraph_bfs(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        node_mapping = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in node_mapping:
                    node_mapping[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                node_mapping[current].neighbors.append(
                    node_mapping[neighbor]
                )

        return node_mapping[node]
