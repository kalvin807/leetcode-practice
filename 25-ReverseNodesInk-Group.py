# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        group_prev = dummy
        l, r = head, head
        while True:
            cnt = 0
            while r and cnt < k:
                r = r.next
                cnt += 1
            if cnt == k:
                pre, cur = r, l
                # Reverse section
                for _ in range(k):
                    temp, cur.next = cur.next, pre
                    pre, cur = cur, temp
                # Link section head and tail
                group_prev.next = pre # pre is the original next node, because line 20 will advance 1 more step
                group_prev = l # l now become the tail
                l = r # r is the next node
            else:
                return dummy.next
# Time compexity = O(2n), first n for iternate over list, second n is sum of reverse actions
# Space compexity = O(1)
