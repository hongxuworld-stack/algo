class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        def reverseList(node):
            pre = None
            cur = node

            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            return pre

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None

        right = reverseList(right)
        left = head

        while right:
            l_next = left.next
            r_next = right.next

            left.next = right
            right.next = l_next

            left = l_next
            right = r_next