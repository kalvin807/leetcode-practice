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

        dummy = Node(-1)
        nodes = {None: None}

        prev = dummy
        cur = head
        while cur:
            clone = Node(cur.val, None, cur.random)
            prev.next = clone
            nodes[cur] = clone  # old to new mapping
            prev = clone
            cur = cur.next

        cur = dummy
        while cur:
            cur.random = nodes[cur.random]  # replace old node with new node via map
            cur = cur.next

        return dummy.next
