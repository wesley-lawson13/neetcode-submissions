# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(r1, r2):

            if not r1 and not r2:
                return True

            if (
                r1 and not r2 or
                r2 and not r1 or
                r1.val != r2.val
            ):
                return False

            left = isSame(r1.left, r2.left)
            right = isSame(r1.right, r2.right)
            return left and right

        if not subRoot:
            return True

        if not root:
            return False

        if isSame(root, subRoot):
            return True
        
        left, right = self.isSubtree(root.left, subRoot), self.isSubtree(root.right, subRoot)
        return left or right
