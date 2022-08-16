import random


class RandomizedSet:
    def __init__(self):
        self.idx_map = {}
        self.value_list = []

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False
        self.value_list.append(val)
        self.idx_map[val] = len(self.value_list) - 1
        return True

    def remove(
        self, val: int
    ) -> bool:  # Trick is to first swap the elm that wanna del to last pos in list then pop it
        if not val in self.idx_map:
            return False
        target_idx = self.idx_map[val]
        # Swap value in list
        last_elm_idx = len(self.value_list) - 1
        last_elm = self.value_list[last_elm_idx]
        self.value_list[last_elm_idx], self.value_list[target_idx] = val, last_elm
        # Update last elm's idx
        self.idx_map[last_elm] = target_idx
        # Remove from list and delete the mapping
        self.value_list.pop()  # O(1) when poping last elm in list
        del self.idx_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.value_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
