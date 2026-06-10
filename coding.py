class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(node):
            pre = None
            cur = node
            while cur:
                nxt = cur.next
                pre.next = cur
                pre = cur
                cur = nxt
            return pre
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        left = head
        right = reverseList(right)
        while right:
            left_nxt = left.next
            right_nxt = right.next
            left.next = right
            left.next.next = left_nxt
            left = left_nxt
            right = right_nxt