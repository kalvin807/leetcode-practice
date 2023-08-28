from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        count = 0
        a, b = float("-inf"), float("-inf")
        for c, d in pairs:
            if b < c:
                count += 1
                a, b = c, d
        return count


test_cases = [
    {
        "pairs": [[1, 2], [2, 3], [3, 4]],
        "expected": 2,
    },
    {
        "pairs": [[1, 2], [7, 8], [4, 5]],
        "expected": 3,
    },
]

if __name__ == "__main__":
    for test_case in test_cases:
        pairs, expected = test_case["pairs"], test_case["expected"]
        got = Solution().findLongestChain(pairs)
        if got != expected:
            print(f"FAILED: test_case: {test_case}, got: {got}")
