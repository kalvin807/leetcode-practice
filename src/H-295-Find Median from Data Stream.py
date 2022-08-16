import heapq


class MedianFinder:
    def __init__(self):
        self.minHeap = []  # for the larger half
        self.maxHeap = []  # for the small half

    def addNum(self, n: int) -> None:
        minHeap, maxHeap = self.minHeap, self.maxHeap
        heapq.heappush(maxHeap, -heapq.heappushpop(minHeap, n))
        if len(minHeap) < len(maxHeap):
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))

    def findMedian(self) -> float:
        minHeap, maxHeap = self.minHeap, self.maxHeap
        if len(maxHeap) < len(minHeap):
            return float(minHeap[0])
        else:
            return (-maxHeap[0] + minHeap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
