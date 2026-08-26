# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_mp = {val : i for i, val in enumerate(inorder)}
        self.pre_i = 0

        def dfs(l, r):
            if l > r:
                return

            val = preorder[self.pre_i]
            self.pre_i += 1
            node = TreeNode(val, None, None)
            
            
            mid = inorder_mp[val]
            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1, r)
            return node

        return dfs(0, len(preorder)-1)
        