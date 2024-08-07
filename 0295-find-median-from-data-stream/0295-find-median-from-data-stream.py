class MedianFinder:

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, (-1 * num))
        
        #1. values in maxHeap are smaller then values in minHeap
        if (self.maxHeap and self.minHeap and (-1 * self.maxHeap[0]) > self.minHeap[0]):
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        
        #2. diff between lengths of the two heaps is greater than 1
        if(len(self.maxHeap) > len(self.minHeap) + 1):
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        
        if(len(self.minHeap) > len(self.maxHeap) + 1):
            val = -1 * heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)
        

    def findMedian(self) -> float:
        if(len(self.maxHeap) > len(self.minHeap)):
            return -1 * self.maxHeap[0]
        if(len(self.minHeap) > len(self.maxHeap)):
            return self.minHeap[0]
        
        return (-1 * self.maxHeap[0] +  self.minHeap[0]) / 2 
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()