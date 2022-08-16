class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = ""
        while i >= 0 or j >= 0 or carry:
            v1 = int(a[i]) if i >= 0 else 0
            v2 = int(b[j]) if j >= 0 else 0
            total = v1 + v2 + carry
            c, carry = str(total % 2), total // 2
            result += c
            i -= 1
            j -= 1
        return result[::-1]
