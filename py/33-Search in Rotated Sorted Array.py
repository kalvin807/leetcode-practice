class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            # Test which side is sorted
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]: 
                    # Scope down to the sorted range if it is in that range
                    right = mid - 1
                else:
                    # Otherwise keep searching in Rotated parts
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
