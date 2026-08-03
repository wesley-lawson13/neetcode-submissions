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
        
        old_to_new = defaultdict(lambda: Node(0))
        old_to_new[None] = None

        cur = head
        while cur: 
            """Idea: Get the new node (by indexing into the old_to_new mp on
                    cur), and update its val and pointers, and get or create
                    the new node for the pointers by using the old cur's 
                    .next or .random values
            """
            old_to_new[cur].val = cur.val
            old_to_new[cur].next = old_to_new[cur.next]
            old_to_new[cur].random = old_to_new[cur.random]
            cur = cur.next

        return old_to_new[head]