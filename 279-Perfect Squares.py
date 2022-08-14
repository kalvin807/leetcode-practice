import collections
class Solution:
    def numSquares(self, n: int) -> int:
        sq_n = [x * x for x in range(1, n + 1) if x * x <= n]
        if not n:
            return 0
        # Starting at 0 coin, and 0 amount
        # Add coin one by one in BFS way
        seen = set()
        queue = collections.deque([(0, n)])
        while queue:
            curCnt, curAmt = queue.popleft()
            curCnt += 1
            x = 1
            for sq_x in sq_n:
                nextAmt = curAmt - sq_x
                if nextAmt == 0:
                    return curCnt
                if nextAmt > 0 and nextAmt not in seen:
                    seen.add(nextAmt)
                    queue.append((curCnt, nextAmt))
