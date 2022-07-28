class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums):
            return (-1, -1)
        
        def bin_search(n):
            l, r = 0, len(nums)
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] >= n:
                    r = mid
                else:
                    l = mid + 1
            return l
        lo = bin_search(target)
        # Find pos of target + 1 then -1 idx will be upper end of target
        return (lo, bin_search(target + 1) - 1) if lo < len(nums) and nums[lo] == target else (-1, -1)
    
    # Time complexity = O(2logn), it does two time
    # Space complexity = O(1)
