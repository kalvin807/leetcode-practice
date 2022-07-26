# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode()
        prev = dummy
        current = head
        while current: 
            # Store temp
            node_a = current
            node_b = current.next
            if node_b == None: # Odd number case
                break
            node_b_next = node_b.next
            # Swap nodes
            prev.next = node_b
            node_b.next = node_a
            node_a.next = node_b_next
            # Advance to next pair
            prev = node_a
            current = node_b_next
        return dummy.next
      # Time complexity: O(n/2), take two node at a time
      # Space complexity: O(1)
