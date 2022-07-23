class Solution:
    def longestPalindrome(self, s: str) -> str:
        isPalindorome = [[False] * len(s) for _ in range(len(s))]
        longest = s[0]
        s_len = len(s)
        # 1 char case -> all of them are palindorme
        for i in range(s_len):
            isPalindorome[i][i] = True
        # 2 neighbour char case -> palindorme if they are the same
        for i in range(s_len - 1):
            if s[i] == s[i + 1]:
                isPalindorome[i][i+1] = True
                longest = s[i:i + 1 + 1]
        # more than 2 char -> check sub string is isPalindorome and head == tail 
        size = 2
        while size < s_len:
            i = 0
            while i < s_len - size:
                start, end = i, i + size
                res = isPalindorome[start + 1][end - 1] and s[start] == s[end]
                if res:
                    longest = s[start : end + 1]
                isPalindorome[start][end] = res
                i += 1
            size += 1
        return longest
# Time complexity = O(n^2) , only loop over the string twice to get all combination, but since we stored substring result, so no need to futher loop for substring problem
# Space complexity = O(n^2)
