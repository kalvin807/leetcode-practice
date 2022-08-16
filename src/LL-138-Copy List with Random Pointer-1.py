"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        dummy = Node(0)
        memo = {None: None}
        prev = dummy
        origin = head
        while origin:
            clone = Node(origin.val)
            prev.next = clone
            memo[origin] = clone
            origin = origin.next
            prev = clone

        clone = dummy.next
        origin = head
        while origin and clone:
            clone.random = memo[origin.random]
            clone = clone.next
            origin = origin.next

        return dummy.next
