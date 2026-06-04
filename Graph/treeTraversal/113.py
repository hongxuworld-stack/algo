# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [[node.val]]
            left_node_list = dfs(node.left)
            right_node_list = dfs(node.right)
            node_list = []
            for lst in left_node_list:
                node_list.append([node.val] + lst)
            for lst in right_node_list:
                node_list.append([node.val] + lst)
            return node_list

        root_node_list = dfs(root)
        res = []
        for lst in root_node_list:
            if sum(lst) == targetSum:
                res.append(lst)
        return res