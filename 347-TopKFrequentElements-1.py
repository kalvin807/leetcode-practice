import collections
import heapq

# This use heap, pq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(int)
        for n in nums: # O(n)
            freq[n] += 1
        pq = [(-value, key) for key, value in freq.items()]
        heapq.heapify(pq) # O(n)
        
        return [heapq.heappop(pq)[1] for _ in range(k)] #O(klogn)
