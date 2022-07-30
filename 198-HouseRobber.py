class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        with
        decision_mem[0] = nums[0] # init case
        decision_mem[1] = max(nums[0], nums[1]) # init case
        # Things to consider when rob i
        # rob i + i - 2 earn more
        # or rob i - 1 earn more
        # or just rob this house (if all postive, then no need to consider, because i - 2 always +ve)
        for i in range(2, len(nums)):
            decision_mem[i] = max(nums[i] + decision_mem[i - 2], decision_mem[i - 1])
        return decision_mem[-1]
# Time complexity = O(n), Space O(n)
class Solution1:
  def rob(self, nums: List[int]) -> int:
      if len(nums) == 1:
          return nums[0]
      last_last = nums[0]
      best = max(nums[0], nums[1]) # init case

      # Things to consider when rob i
      # rob i + i - 2 earn more
      # or rob i - 1 earn more
      # or just rob this house (if all postive, then no need to consider, because i - 2 always +ve)
      for i in range(2, len(nums)):
          best, last_last = max(nums[i] + last_last, best), best
      return best
# Time complexity = O(n), Space O(1)
# Personally think this is less readable and initutive. 
