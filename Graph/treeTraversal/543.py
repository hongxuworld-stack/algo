class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.left)
            res = max(res,left + right +1)
            return max(left,right) + 1
        dfs(root)
        return res