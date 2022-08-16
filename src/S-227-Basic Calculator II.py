class Solution:
    def calculate(self, s: str) -> int:
        s += "#"  # End of eq
        stack = []
        num = 0
        sign = "+"
        for c in s:
            if c.isdigit():
                # add to current num counter
                num = num * 10 + int(c)
            if c in "+-*/#":
                if sign == "+":
                    stack.append(num)
                if sign == "-":
                    stack.append(-num)
                if sign == "*":
                    stack.append(stack.pop() * num)
                if sign == "/":
                    stack.append(int(stack.pop() / num))
                sign = c
                num = 0
        return sum(stack)
