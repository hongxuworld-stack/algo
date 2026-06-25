class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_dict = {0: 1}
        res = 0
        def dfs(node,cur_sum):
            nonlocal res
            if not node:
                return
            cur_sum += node.val
            target = cur_sum - targetSum
            if target in prefix_dict:
                res += prefix_dict[target]
            prefix_dict[cur_sum] = prefix_dict.get(cur_sum,0) + 1
            dfs(node.left,cur_sum)
            dfs(node.right,cur_sum)
            prefix_dict[cur_sum] -= 1
        dfs(root,0)
        return res