"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
import collections


class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        tree = {}
        for e in employees:
            tree[e.id] = e
        queue = collections.deque([tree[id]])
        importance = 0
        while queue:
            for _ in range(len(queue)):
                e = queue.popleft()
                importance += e.importance
                for sub_id in e.subordinates:
                    queue.append(tree[sub_id])
        return importance

    # BFS, O(n) for making the tree
