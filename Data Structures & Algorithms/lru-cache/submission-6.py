class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nd_map = {}

        self.head = self.tail = Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, nd):
        prev, nxt = nd.prev, nd.next

        prev.next, nxt.prev = nxt, prev

    def insert(self, nd):
        # insert always at the tail
        prev, nxt = self.tail.prev, self.tail

        prev.next, nxt.prev = nd, nd
        nd.prev, nd.next = prev, nxt

    def get(self, key: int) -> int:
        if key not in self.nd_map:
            return -1

        nd = self.nd_map[key]
        self.remove(nd)
        self.insert(nd)
        return nd.val
            
    

    def put(self, key: int, value: int) -> None:
        if key in self.nd_map:
            self.remove(self.nd_map[key])
        
        self.nd_map[key] = Node(key, value)
        self.insert(self.nd_map[key])
        if len(self.nd_map) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.nd_map[lru.key]
        
        
