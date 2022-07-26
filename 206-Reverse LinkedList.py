# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        pre, cur = None, head
        while cur:
            # Point next to prev node (reverse)
            temp, cur.next = cur.next, pre
            # advance to next node, advance prev to current
            cur, pre = temp, cur
        return pre # last pointer will be the head
    # Time complexity = O(n)
    # Space complexity = O(1)
