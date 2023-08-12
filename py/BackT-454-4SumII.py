import collections


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        # split into (a + b) + (c + d)
        # get all combo of a + b and try plus with c + d
        combo = collections.defaultdict(int)
        for a in nums1:  # O(n^2)
            for b in nums2:
                combo[a + b] += 1  # number of a + b combo can result in this combo
        cnt = 0
        for c in nums3:  # O(n^2)
            for d in nums4:
                if (comp := -c - d) in combo:
                    cnt += combo.get(comp, 0)
        return cnt  # O(n^2)
