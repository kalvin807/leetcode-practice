# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = [] 
        for i, ll in enumerate(lists):
            node = ll
            j = 0
            while node:
                # Compare node by following piority, val, idx of list, idx of node in list
                # Leetcode do not require to sort by list and node index
                # It is used to resolve case where nodes' val is same across same list or list array
                pq.append((node.val, i, j, node))
                node = node.next
                j += 1
                
        heapq.heapify(pq) # A min heap, smaller item will come first, O(total number of node), in-place sort
        # Now the pq is sorted by value, pop them 1 by 1 and create the sorted list
        root, current = None, None
        while len(pq):
            _, _, _, node = heapq.heappop(pq)
            if not current:
                current = node
                root = node
            else:
                current.next = node
                current = node
        # Last node should connect to nothing
        if current:
            current.next = None
        return root
    # Time complexity: O(total number of node), should be best
    # Space complexity: O(total number of node), not best, using merge sort and achieve O(1)
    # Not ideal, but it works,
