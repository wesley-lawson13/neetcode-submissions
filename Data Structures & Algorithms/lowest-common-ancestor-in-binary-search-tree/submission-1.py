# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        L, R = p.val, q.val
        if L > R:
            L, R = R, L

        def bin_search(root):

            # different side case
            if L <= root.val and root.val <= R:
                return root

            if L > root.val:
                return bin_search(root.right)

            return bin_search(root.left)

        
        return bin_search(root)

    

        

        