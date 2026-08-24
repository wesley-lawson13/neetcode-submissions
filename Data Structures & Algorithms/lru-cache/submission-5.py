class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val

        self.prev, self.next = None, None

class LRUCache:


    def __init__(self, capacity: int):
        self.cap = capacity
        self.i_mp = {}

        self.head, self.tail = Node(-1, 0), Node(-1, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key not in self.i_mp:
            return -1

        node = self.i_mp[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.i_mp:
            node = self.i_mp[key]
            self.remove(node)
        
        new = Node(key, value)
        self.i_mp[key] = new
        self.insert(new)
        if len(self.i_mp) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.i_mp[lru.key]


        
