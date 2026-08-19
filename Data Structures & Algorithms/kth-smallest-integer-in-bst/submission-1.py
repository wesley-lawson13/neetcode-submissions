# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ret = []
        def dfs_and_insert(node): # pos is prepend or append
            if not node:
                return
            
            dfs_and_insert(node.left)
            ret.append(node.val)
            dfs_and_insert(node.right)

        dfs_and_insert(root)
        return ret[k-1]

            

            


        
