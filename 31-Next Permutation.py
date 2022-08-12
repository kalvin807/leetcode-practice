class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i , j = len(nums) - 1, len(nums) - 2
        while j >= -1 and nums[j] >= nums[i]:
            i -= 1
            j -= 1
        # i: first digit of the decreasing sequence
        # j: last digit of non-decreasing sequence
        # Swap j with a larger elem
        if j > -1:
            i = len(nums) - 1
            while i > -1 and nums[i] <= nums[j]:
                i -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # Reverse the decreasing seq to make it smallest
        l, r = j + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums
