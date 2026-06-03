class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,min_val,max_val):
            if not node:
                return True
            if not min_val<node.val<min_val:
                return False
            return dfs(node.left,min_val,node.val) and dfs(node.right,node.val,max_val)
        dfs(root,float("-inf"),float("inf"))