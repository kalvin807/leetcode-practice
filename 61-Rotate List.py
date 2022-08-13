# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k == 0:
            return head
        prev = None
        node = head
        size = 0
        while node:
            size += 1
            prev = node
            node = node.next
        prev.next = head
            
        k = k % size
        node = head
        for _ in range(size - k - 1):
            node = node.next
        temp = node.next
        node.next = None
        return temp
