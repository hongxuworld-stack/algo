from collections  import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        numOfNode = len(graph)
        indegree = [0] * numOfNode
        reverse_graph = [[] for _ in range(numOfNode)]
        q = deque()
        for source_node,end_nodes in enumerate(graph):
            for end_node in end_nodes:
                reverse_graph[end_node].append(source_node)
                indegree[source_node] += 1
        res = []
        for  i in range(len(indegree)):
            if  indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            res.append(node)
            for nxt_node in reverse_graph[node]:
                indegree[nxt_node] -= 1
                if indegree[nxt_node] == 0:
                    q.append(nxt_node)
        return sorted(res)