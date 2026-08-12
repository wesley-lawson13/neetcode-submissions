# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        def depth(node):

            if not node:
                return 0
            
            return max(depth(node.left), depth(node.right))+1

        q = deque()
        q.append(root)
        while q:
            pop = q.popleft()
            left = depth(pop.left)
            right = depth(pop.right)
            if abs(left-right) > 1:
                return False

            if pop.left:
                q.append(pop.left)
            
            if pop.right:
                q.append(pop.right)

        return True

        