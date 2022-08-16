import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        most_common = cnt.most_common(k)  # Return top k most common item (n, freq)
        return [itm[0] for itm in most_common]
