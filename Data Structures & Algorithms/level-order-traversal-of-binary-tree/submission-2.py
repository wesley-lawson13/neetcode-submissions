# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        
        q = deque()
        q.append(root)

        while q:
            
            # the number of nodes on the level will be the length of the q
            num_on_level = len(q)
            level = []
            for i in range(num_on_level):
                pop = q.popleft()
                if pop:
                    level.append(pop.val)
                    q.append(pop.left)
                    q.append(pop.right)
            if level:
                res.append(level)

        return res

            
            
            
