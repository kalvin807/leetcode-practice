class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            memo[0][i] = 1
        for i in range(n):
            memo[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

        return memo[-1][-1]


if __name__ == "__main__":
    cases = [
        {"m": 3, "n": 2, "expect": 3},
        {"m": 1, "n": 1, "expect": 1},
        {"m": 7, "n": 3, "expect": 28},
        {"m": 23, "n": 12, "expect": 193536720},
    ]

    for c in cases:
        result = Solution().uniquePaths(c["m"], c["n"])
        if result == c["expect"]:
            print("OK")
        else:
            print(f"FAIL expect: {c['expect']} got: {result}")
