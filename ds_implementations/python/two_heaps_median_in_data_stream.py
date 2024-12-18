import heapq

class MedianFinder:

  def __init__(self):
    self.maxHeap = []
    self.minHeap = []

  def addNum(self, num: int) -> None:
    if not self.maxHeap or num <= -self.maxHeap[0]: heapq.heappush(self.maxHeap, -num)
    else: heapq.heappush(self.minHeap, num)

    if len(self.maxHeap) > len(self.minHeap) + 1: heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
    elif len(self.minHeap) > len(self.maxHeap): heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

  def findMedian(self) -> float:
    if len(self.maxHeap) == len(self.minHeap): return (-self.maxHeap[0] + self.minHeap[0]) / 2
    else: return -self.maxHeap[0]