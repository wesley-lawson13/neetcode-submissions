"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return
        
        old_to_new = {} # maps old to new node
        
        q = deque()
        q.append(node)
        processed = set()

        while q:
            old = q.popleft()

            if old in old_to_new:
                cur = old_to_new[old]
            else:
                cur = Node(old.val)
                old_to_new[old] = cur

            for nei in old.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                
                new = old_to_new[nei]
                if new in processed:
                    continue
                
                # connect both ways (undirected)
                cur.neighbors.append(new)
                new.neighbors.append(cur)

                # add to the queue to be processed
                q.append(nei)
            processed.add(cur)

        return old_to_new[node]

        