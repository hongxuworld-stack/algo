# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        def helper(node):
            if not node:
                return
            left_node = node.left
            right_node = node.right
            node.left = helper(right_node)
            node.right = helper(left_node)
            return node
        helper(root)
        return root