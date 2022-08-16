class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        # Multiply ans i using with last sum and last idx
        current = 1
        for i in range(0, len(nums), 1):
            ans[i] *= current
            current *= nums[i]
        current = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= current
            current *= nums[i]
        return ans
