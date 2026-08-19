# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class ListNode:

    def __init__(self, val):
        self.val = val
        self.prev, self.next = None, None

class Solution:

    def prepend(self, last, new):
        prev, nxt = last.prev, last
        prev.next, nxt.prev = new, new
        new.prev, new.next = prev, nxt
        
    def append(self, last, new):
        prev, nxt = last, last.next
        prev.next, nxt.prev = new, new
        new.prev, new.next = prev, nxt
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs_and_insert(node, last, pre): # pos is prepend or append
            if not node:
                return
            
            new = ListNode(node.val)
            if pre:
                self.prepend(last, new)
            else:
                self.append(last, new)

            left = dfs_and_insert(node.left, new, True)
            right = dfs_and_insert(node.right, new, False)
            return

        head, tail = ListNode(0), ListNode(0)
        head.next, tail.prev = tail, head

        dfs_and_insert(root, head, False)
        cur = head
        while k > 0:

            cur = cur.next
            k -= 1

        return cur.val

            

            


        
