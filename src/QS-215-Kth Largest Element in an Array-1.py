import random


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k

        def partition(l, r):
            rng = random.randint(l, r)
            nums[rng], nums[r] = nums[r], nums[rng]
            x = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] <= x:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def quickSelect(l, r):
            pivot = partition(l, r)
            if pivot == k:
                return nums[pivot]
            elif pivot > k:
                return quickSelect(l, pivot - 1)
            else:
                return quickSelect(pivot + 1, r)

        return quickSelect(0, len(nums) - 1)
