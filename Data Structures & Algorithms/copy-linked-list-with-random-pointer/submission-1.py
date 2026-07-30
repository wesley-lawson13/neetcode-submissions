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
        
        dummy = Node(-1, None, None)
        cur = dummy

        rand_old_to_new = {}
        unseen_rands = {}

        while head:
            new = Node(head.val, None, None)
            if head.random and head.random in rand_old_to_new: 
                # seen in the old to new conversion
                new_rand = rand_old_to_new[head.random]
                new.random = new_rand
            elif head.random: # has a rand but hasn't been seen yet
                unseen_rands[new] = head.random
                print(f"unseen rands adding key (new) {new.val} = (old {head.random.val}")
            
            # Add the head to the map for later values
            rand_old_to_new[head] = new

            cur.next = new
            cur = cur.next
            head = head.next

        for key in unseen_rands:
            new_rand = unseen_rands[key]
            print(f"updating this node: {new_rand.val}")
            key.random = rand_old_to_new[new_rand]

        return dummy.next

        





