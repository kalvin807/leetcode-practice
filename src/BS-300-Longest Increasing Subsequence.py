class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = []  # This store the subsequence
        def bin_search(arr, target):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l # when there is no match; either target is smaller or larger than all element in memo
            
        for n in nums:
            res = bin_search(memo, n)
            if res == len(memo):
                memo.append(n)
            else:
                memo[res] = n # update the lowest value or the found value
        return len(memo)
