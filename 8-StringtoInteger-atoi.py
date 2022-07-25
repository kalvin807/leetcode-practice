class Solution:
    UPPER = 2 ** 31 - 1
    LOWER = 2 ** 31 * -1
    digits = set(n for n in "12345667890")
    signs = set(["+", "-"])
    
    
    def myAtoi(self, s: str) -> int:
        # Starting state
        state = 0
        n_start, n_end = None, None
        sign = 1
        for i, c in enumerate(list(s)):
            if state == 0: # White space
                if c == " ":
                    continue
                else:
                    if c in self.digits:
                        n_start = i
                        state = 1
                    elif c in self.signs:
                        sign = 1 if c == "+" else -1
                        state = 2
                    else:
                        n_end = i
                        break
            elif state == 1: # Digit
                if not c in self.digits:
                    n_end = i
                    break
            elif state == 2: # Sign
                if not c in self.digits:
                    n_end = i 
                    break
                else:
                    n_start = i
                    state = 1
            n_end = i + 1
        if n_start == None or n_end == None:
            return 0
        
        n = 0
        sig = 0
        bound = self.UPPER if sign > 0 else self.LOWER
        i = n_end - 1
        
        
        while i >= n_start:
            d = s[i]
            diff = int(d) * (10 ** sig)
            # out of bound check
            if diff > abs(bound - n):
                return bound
            n += diff if sign > 0 else -diff
            sig += 1
            i -= 1
        return n
      
     # Time complexity = O(n)
     # Space complexity = O(1) 
        
        
