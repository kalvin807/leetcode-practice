class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        levels = ["" for _ in range(numRows)]
        goDown = False
        l = 0
        for c in s:
            levels[l] += c
            # Flip direction when we reach top or bottom
            if l == 0 or l == numRows - 1:
                goDown = not goDown
            l += 1 if goDown else -1
        return "".join(levels)
    # Time complexity = O(n)
    # Space complexity = O(n)
    # n = number of char in string
