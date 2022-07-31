import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        # put to the end of delete queue
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if self.capacity == 0: # Fulled, delete LRU item
                self.cache.popitem(last=False) # Pop first item in queue
                self.capacity += 1
            self.cache[key] = value
            self.capacity -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
