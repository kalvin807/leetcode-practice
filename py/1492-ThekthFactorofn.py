class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for m in range(1, n + 1):
            if n % m == 0:
                k -= 1
            if k == 0:
                return m
        return -1


# Trivial way to do this, Time O(n), space O(1)
class Solution2:
    def kthFactor(self, n: int, k: int) -> int:
        # Math trick
        # if an int m that is n % m == 0
        # then n % m^2 also == 0
        for m in range(1, int(n**0.5) + 1):
            if n % m == 0:
                k -= 1
            if k == 0:
                return m
        for m in range(int(n**0.5), 0, -1):
            if m * m >= n:
                continue
            if n % m == 0:
                k -= 1
            if k == 0:
                return n // m
        return -1


# Math way to do this, Time O(2sqrt(n)), space O(1)
