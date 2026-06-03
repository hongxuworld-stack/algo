class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        res = float("inf")

        def inorder(node):
            nonlocal prev, res
            if not node:
                return
            # left
            inorder(node.left)
            # root
            if prev is not None:
                res = min(res, node.val - prev)
            prev = node.val
            # right
            inorder(node.right)
        inorder(root)
        return res