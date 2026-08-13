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

        q = deque()
        q.append(root)

        while q:
            pop = q.popleft()

            if pop.val == subRoot.val and isSame(pop, subRoot):
                return True
            
            if pop.left:
                q.append(pop.left)
            if pop.right:
                q.append(pop.right)

        return False
