class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        size = len(nums) + 1
        for r, n in enumerate(nums):
            total += n
            # try trim subarray when total >= target
            while total >= target:
                size = min(size, r - l + 1)
                total -= nums[l]
                l += 1
        return size if size <= len(nums) else 0
    # Time complexity = O(n)
    # Space = O(1)
