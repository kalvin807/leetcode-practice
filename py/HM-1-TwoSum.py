class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i, n in enumerate(nums):
            need = target - n
            if need in comp:
                return [i, comp[need]]
            comp[n] = i
