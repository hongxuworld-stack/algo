class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        # 左子树为空，只能走右边
        if not root.left:
            return right_depth + 1
        
        # 右子树为空，只能走左边
        if not root.right:
            return left_depth + 1
        
        # 左右都存在，才可以取 min
        return min(left_depth, right_depth) + 1