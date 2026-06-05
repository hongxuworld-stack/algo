# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# all records
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#         def dfs(node):
#             if not node:
#                 return []
#             if not node.left and not node.right:
#                 return [[node.val]]
#             left_node_list = dfs(node.left)
#             right_node_list = dfs(node.right)
#             node_list = []
#             for lst in left_node_list:
#                 node_list.append([node.val] + lst)
#             for lst in right_node_list:
#                 node_list.append([node.val] + lst)
#             return node_list

#         root_node_list = dfs(root)
#         res = []
#         for lst in root_node_list:
#             if sum(lst) == targetSum:
#                 res.append(lst)
#         return res

#dfs travel
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node,path,cur_sum):
            if not node:
                return
            path.append(node.val)
            cur_sum += node.val
            if not node.left and not node.right:
                if cur_sum == targetSum:
                    res.append(path[:])
            dfs(node.left,path,cur_sum)
            dfs(node.right,path,cur_sum)
            path.pop()
        dfs(root,[],0)
        return res
