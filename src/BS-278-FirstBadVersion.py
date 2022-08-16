# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1  # first version
        right = n  # last versiion
        first_bad = n

        while left <= right:
            mid = left + (right - left) // 2

            # Test mid point
            # If mid point bad -> all behind mid is bad, test eailier copy for first bad
            # If mid point good -> bad is somewhere behind mid, test later copy for bad version
            # Loop until left and right is at the same version
            if isBadVersion(mid):
                right = mid - 1
                first_bad = mid
            else:
                left = mid + 1

        return first_bad


# Time complexity:  O(log(n)), at most will use log(n) time to find in the tree
# Space complexity: O(1), only use constant amount of ram to store pointers
# Example: [1, 2, 3, 4, 5], Bad: 3
#  1 - 5 , try 3 -> 3 is bad -> Range become 1 - 2
#  1 - 2 , try 2 -> 2 is good -> Range become 3 - 2
#  Loop end -> return 3 -> ok

# Example: [1]， Bad: 1
# 1 - 1, try 1 -> 1 is bad -> Range become 1 - 0
# Loop end return 1 -> ok

# Example: [1, 2, 3, 4, 5], Bad: 4
#  1 - 5 , try 3 -> 3 is good -> Range become 4 - 5
#  4 - 5 , try 4 -> 4 is bad -> Range become 4 - 3
#  Loop end -> return 4 -> ok
