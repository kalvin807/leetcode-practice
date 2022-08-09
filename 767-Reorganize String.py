import collections, heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        pieces = collections.defaultdict(int)
        for c in s:
            pieces[c] += 1
        
        items = [(-v, k) for k, v in pieces.items()]
        heapq.heapify(items)
        ans = ""
        prev = None
        
        while len(items):
            cnt, c = heapq.heappop(items)
            if prev and prev[0] < 0:
                heapq.heappush(items, prev)
            ans += c
            prev = (cnt + 1, c)
        
        return ans if len(ans) == len(s) else ""
