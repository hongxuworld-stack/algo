# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path = []
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                res += int("".join(map(str,path)))
            path.pop()
        dfs(root)
        return res