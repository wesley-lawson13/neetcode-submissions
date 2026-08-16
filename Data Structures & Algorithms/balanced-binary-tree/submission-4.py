# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node): # returns isBalanced, height
            
            if not node:
                return [True, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            isBalanced = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)
            return [isBalanced, max(left[1], right[1])+1]

        ret = dfs(root)
        return ret[0]