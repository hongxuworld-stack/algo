class Solution:
    # def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    #     prev = None
    #     res = float("inf")

    #     def inorder(node):
    #         nonlocal prev, res
    #         if not node:
    #             return
    #         # left
    #         inorder(node.left)
    #         # root
    #         if prev is not None:
    #             res = min(res, node.val - prev)
    #         prev = node.val
    #         # right
    #         inorder(node.right)
    #     inorder(root)
    #     return res

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res_list = []
        res = float("inf")
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            res_list.append(node.val)
            inOrder(node.right)
        inOrder(root)
        for i in range(1,len(res_list)):
            res = min(res,res_list[i] - res_list[i-1])
        return res