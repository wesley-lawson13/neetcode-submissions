# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        q = deque()
        q.append(root)

        max_diam = 0
        while q:
            new = q.popleft()
            depth_left = self.maxDepth(new.left)
            depth_right = self.maxDepth(new.right)
            max_diam = max(max_diam, depth_left + depth_right)

            if new.left:
                q.append(new.left)
            if new.right:
                q.append(new.right)

        return max_diam

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        return max(left, right)