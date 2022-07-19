class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        left, right = 0, len(n) - 1
        
        while left < right:
            total = n[left] + n[right]
            if total == t:
                # 1 indexed
                return [left + 1, right + 1]
            elif total < t:
                # sum too small, increase smaller side
                left += 1
            else:
                # sum too big, decrease bigger side
                right -= 1
        # O(n)
