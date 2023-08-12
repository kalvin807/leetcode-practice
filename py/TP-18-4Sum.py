class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)):  # n
            for j in range(i + 1, len(nums)):  # n
                left = j + 1
                right = len(nums) - 1
                while left < right:  # n
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    # Tweak pointer by size
                    elif total > target:
                        right -= 1
                    else:
                        left += 1
        return list(ans)  # O(n^3)
