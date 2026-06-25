from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        q = deque()
        q.append(root)
        res = None
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if i==0:
                    res = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res