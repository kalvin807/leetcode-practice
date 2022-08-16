class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Smallest element or largest element in original array will always be the largest in squared array
        squared = [0] * len(nums)
        l, r = 0, len(nums) - 1
        i = len(nums) - 1
        while i >= 0:
            # Sort from largest element
            # Everytime pick the bigger one
            if (sq_l := nums[l] * nums[l]) > (sq_r := nums[r] * nums[r]):
                squared[i] = sq_l
                l += 1
            else:
                squared[i] = sq_r
                r -= 1
            i -= 1
        return squared

    # Time complexity : O(n), it will walk all elements to generate a complete squared array
    # Space complexity: O(n), it use a new arr to store ans
