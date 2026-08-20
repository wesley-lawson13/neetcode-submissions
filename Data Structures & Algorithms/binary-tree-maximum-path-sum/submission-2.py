# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = float('-inf')
        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            ret_val = max(left_sum + node.val, right_sum + node.val, node.val)

            self.max_sum = max(left_sum + right_sum + node.val, self.max_sum, ret_val)
            return ret_val

        dfs(root)
        return self.max_sum