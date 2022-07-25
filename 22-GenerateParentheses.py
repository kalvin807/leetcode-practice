class Solution:
    def generate(self, s, open, close):
        # Stop when the size is met, all pair generated
        if len(s) == self.size:
            self.combo.add(s)
        # Keep track of open and close count.    
        # Only attempt to create next state if the combo is valid
        if open > 0: 
            self.generate(s + "(", open - 1, close + 1)
        if close > 0:
            self.generate(s + ")", open, close - 1)
    
    def generateParenthesis(self, n: int) -> List[str]:
            self.combo = set()
            self.size = n * 2
            # Drive by adding first open bracket
            self.generate("(", n - 1 , 1)
            return self.combo
    # Time complexity = O(n * 2) ? each valid combo is n * 2 long in at most n step
    # Space complexity = O(n)
