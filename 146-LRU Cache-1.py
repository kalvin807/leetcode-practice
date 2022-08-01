class Node:
    def __init__(self, key, value, next, prev):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node
            
        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node

        node.next, node.prev = None, None
    
    def pop(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        if self.head: # guard if next is end of list
            self.head.prev = None
        return temp
    
    def insert(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    
        

class LRUCache:
    # Requirements:
    # Read is O(1)
    # Read not found return - 1
    
    # Write when max cap will remove least recent used item
    
    def __init__(self, capacity: int):
        self.max = capacity
        self.cache = {}
        self.queue = DLinkedList()
        self.size = 0

    def get(self, key: int) -> int:
        if node := self.cache.get(key, None):
            # Remove from current pos and put into tail
            self.queue.remove(node)
            self.queue.insert(node)
            return node.value
        else:
            return -1
        
        
        
    def put(self, key: int, value: int) -> None:
        # try update
        if node := self.cache.get(key, None):
            # update value
            node.value = value
            # Remove from current pos and put into tail
            self.queue.remove(node)
            self.queue.insert(node)
            return

        if self.size == self.max:
            lr_node = self.queue.pop()
            self.cache[lr_node.key] = None
            self.size -= 1
        node = Node(key, value, None, None)
        self.queue.insert(node)
        self.cache[key] = node
        self.size += 1
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
