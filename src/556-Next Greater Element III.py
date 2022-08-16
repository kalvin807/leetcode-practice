class Solution:
    def nextGreaterElement(self, n: int) -> int:
        prev = 0
        n_str = list(str(n))
        i = len(n_str) - 1
        while i - 1 >= 0 and n_str[i] <= n_str[i - 1]:
            i -= 1
        if i == 0:
            return (
                -1
            )  # The number is in decresing order, impossible to find a better combo

        # Find a digit that is larger than the first decreasing number
        j = len(n_str) - 1
        while n_str[j] <= n_str[i - 1]:
            j -= 1
        # Swap and form a new string
        # Reverse the desreasing order to minimise the value
        n_str[j], n_str[i - 1] = n_str[i - 1], n_str[j]
        ans = int("".join(n_str[:i] + n_str[i:][::-1]))
        return ans if ans < 2**31 else -1
        # O(n) where n is the number of digit
