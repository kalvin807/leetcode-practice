import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        freq_map = collections.defaultdict(list)
        for n, cnt in counter.items():
            freq_map[cnt].append(n)
        
        topK = []
        for freq in range(len(nums), -1, -1):
            if freq in freq_map:
                topK += freq_map[freq]
            if k == len(topK):
                break
        return topK
    # Time complexity = O(n)
    # Space complexity = O(n)
