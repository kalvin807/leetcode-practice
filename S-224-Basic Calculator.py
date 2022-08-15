class Solution:
    def calculate_recur(self, s: str) -> int:
        def update(sign, n):
            if sign == "+":
                stack.append(num)
            if sign == "-":
                stack.append(-num)
            if sign == "*":
                stack.append(stack.pop() * num)
            if sign == "/":
                stack.append(int(stack.pop() / num))

        stack = []
        sign = "+"
        num = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c == "(":
                num, j = self.calculate_recur(s[i+1:])
                i += j
            elif c == ")":
                update(sign, num)
                return sum(stack), i + 1
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                update(sign, num)
                sign = c
                num = 0
            i += 1
        update(sign, num)
        return sum(stack), None

    def calculate(self, s: str) -> int:
        ans, _ = self.calculate_recur(s)
        return ans
