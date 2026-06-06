
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        counter = 0
        for node in lists:
            if node:
                heapq.heappush(heap,(node.val,counter,node))
                counter += 1
        cur = None
        if not heap:
            return None
        new_node = heap[0][2]
        while len(heap):
            val,_,node = heapq.heappop(heap)
            nxt = node.next
            if cur:
                cur.next = node
                cur = node
            else:
                cur = node
            node.next = None
            if nxt:
                heapq.heappush(heap,(nxt.val,counter,nxt))
                counter += 1
        return new_node
            