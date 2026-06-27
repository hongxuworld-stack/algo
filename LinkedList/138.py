class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node_mapping = {}
        cur_node = head
        while cur_node:
            clone_node = Node(cur_node.val)
            node_mapping[cur_node] = clone_node
            cur_node = cur_node.next
        cur_node = head
        while cur_node:
            clone_node = node_mapping[cur_node]
            clone_node.next = node_mapping.get(cur_node.next)
            clone_node.random = node_mapping.get(cur_node.random)
            cur_node = cur_node.next
        return node_mapping[head]