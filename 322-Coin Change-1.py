import collections
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        # Starting at 0 coin, and 0 amount
        # Add coin one by one in BFS way
        seen = set()
        queue = collections.deque([(0, 0)])
        while queue:
            curCnt, curAmt = queue.popleft()
            # Add coin
            curCnt += 1
            for c in coins:
                nextAmt = curAmt + c
                if nextAmt == amount:
                    return curCnt
                elif nextAmt < amount and nextAmt not in seen:
                    seen.add(nextAmt)
                    queue.append((curCnt, curAmt + c))
        return -1
