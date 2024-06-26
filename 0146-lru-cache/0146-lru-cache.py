class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None
        

class LRUCache:

    #remove node from list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    #insert node at end
    def insert(self, node):
        head = self.tail.prev
        head.next = node
        node.prev = head
        node.next = self.tail
        self.tail.prev = node
        
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    #head-> least recently used, tail-> most recently used
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            leastRecentlyUsed = self.head.next
            self.remove(leastRecentlyUsed)
            del self.cache[leastRecentlyUsed.key]
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)