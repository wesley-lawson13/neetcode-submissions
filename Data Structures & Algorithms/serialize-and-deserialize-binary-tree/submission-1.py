# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        self.ret = []
        def dfs(node):
            if not node:
                self.ret.append("N")
                return

            self.ret.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return

        dfs(root)
        return ",".join(self.ret)

        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        print(data)
        pre = data.split(",")
        self.i = 0
        def dfs():
            if pre[self.i] == "N":
                self.i += 1
                return None

            new = TreeNode(int(pre[self.i]))
            self.i += 1

            new.left = dfs()
            new.right = dfs()
            return new

        root = dfs()
        return root

