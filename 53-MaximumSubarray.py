class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Record largest sum
        # Record starting point
        largest = -float("inf")
        current = -float("inf")
        for j in range(len(nums)):
        # Iterate over the array 
            # Pick largest of
            # only this number
            n = nums[j]
            # with this number
            withN = current + n
            # Update largest sum and starting point accordingly
            current = max(withN, n)
            largest = max(largest, current)
            
        return largest
