class Solution:
    MAX_INT = 2**31-1
    MAX_INT_LIMIT = MAX_INT // 10
    
    def reverse(self, x: int) -> int:
        y = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x != 0:
            r = x % 10
            # check overflow
            if (y > self.MAX_INT_LIMIT): 
                return 0
            if (y == self.MAX_INT_LIMIT and r == 7):
                return 0
            y = y * 10 + r
            x = x // 10

        return y * sign
      # Time Complexity = O(n), n = number of digit
      # Space Complexity = O(1)
