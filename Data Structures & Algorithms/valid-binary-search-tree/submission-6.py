# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False 
        
        def dfs(node, min_bound, max_bound): # types TreeNode, int, int

            if not node:
                return True

            if (node.val <= min_bound or node.val >= max_bound):
                return False

            left = dfs(node.left, min_bound, node.val) # going left, set the max
            right = dfs(node.right, node.val, max_bound) # going right, set the min
            return left and right

        return dfs(root, float('-inf'), float('inf'))

        
                

            
