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

    def copyRandomList_interweaving(
        self, head: 'Optional[Node]'
    ) -> 'Optional[Node]':
        if not head:
            return None

        # Insert each cloned node directly after its original node.
        cur = head
        while cur:
            clone = Node(cur.val)
            clone.next = cur.next
            cur.next = clone
            cur = clone.next

        # The clone of cur.random is cur.random.next.
        cur = head
        while cur:
            clone = cur.next
            clone.random = cur.random.next if cur.random else None
            cur = clone.next

        # Restore the original list and extract the cloned list.
        cur = head
        clone_head = head.next

        while cur:
            clone = cur.next
            cur.next = clone.next
            clone.next = clone.next.next if clone.next else None
            cur = cur.next

        return clone_head
