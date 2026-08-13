class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.i_mp = {}
        self.cap = capacity

        # dummy head and tail values; sit at the 
        # boundary of the LRU linked list and 
        # act to give easy access to the actual
        # first and last items -- these values will
        # never get updated, only their pointers
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    # --- HELPERS ---

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    
    #insert node at the right
    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.i_mp:
            # want to remove it then re-insert it
            node = self.i_mp[key]
            self.remove(node)
            self.insert(node)
            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.i_mp:
            node = self.i_mp[key]
            self.remove(node)
        new = Node(key, value)
        self.i_mp[key] = new
        self.insert(new)

        # if adding this node exceeds the capacity,
        # pop the least recently used from the map and 
        # remove it from the hash map
        if len(self.i_mp) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.i_mp[lru.key]


        
        
        
