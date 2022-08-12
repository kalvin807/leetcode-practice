class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        ans = ""
        carry = 0
        
        idx1, idx2 = len(num1) - 1, len(num2) - 1
        
        while idx1 >= 0 or idx2 >= 0:
            v1 = int(num1[idx1]) if idx1 >= 0 else 0
            v2 = int(num2[idx2]) if idx2 >= 0 else 0
            total = v1 + v2 + carry
            digit, carry = total % 10, total // 10
            ans += str(digit)
            
            idx1 -= 1
            idx2 -= 1
        if carry > 0:
            ans += str(carry)
    
        return ans[::-1]
        
            
            
