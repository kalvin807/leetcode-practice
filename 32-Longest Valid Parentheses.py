class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        stack = [-1]
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxans = max(maxans, i - stack[-1])
        return maxans
