import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        eat = 0
        n = len(apples)
        i = 0
        heap = []
        while True:
            if i < n:
                heapq.heappush(heap, (i + days[i], apples[i]))
            while heap and heap[0][0] <= i:
                heapq.heappop(heap)
            if heap:
                rot, apple = heapq.heappop(heap)
                eat += 1
                if apple > 1:
                    heapq.heappush(heap, (rot, apple-1))
            if not heap and i >= n:
                break
            i += 1
        return eat
