"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        old_to_copy = collections.defaultdict(lambda: Node(0))
        old_to_copy[None] = None

        cur = head

        while cur:
            old_to_copy[cur].val = cur.val # creates a node and sets its value to the cur val
            old_to_copy[cur].next = old_to_copy[cur.next] # makes this none or, if seen already, the actual next node
            old_to_copy[cur].random = old_to_copy[cur.random] # makes this none (if random is none) or creates the node

            cur = cur.next

        return old_to_copy[head] 


        





