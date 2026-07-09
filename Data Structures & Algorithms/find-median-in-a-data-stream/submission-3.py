class MedianFinder:

    def __init__(self):
        self.minHeap = [] # larger array
        self.maxHeap = [] # smaller array

    def addNum(self, num: int) -> None:
        '''
        always append to the maxHeap
        check that max heap peek <= min heap peek
        if not then move it 
        last thing check the length 
        '''
        heapq.heappush(self.maxHeap, num * (-1))
        if(self.minHeap and self.maxHeap[0] * (-1) > self.minHeap[0]):
            popMax = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, popMax * (-1))
        if(len(self.maxHeap) - len(self.minHeap) > 1):
            popMax = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, popMax * (-1))
        if(len(self.minHeap) - len(self.maxHeap) > 1):
            popMin = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, popMin * (-1))
        if(num == 3):
            print(self.minHeap)
            print(self.maxHeap)
    def findMedian(self) -> float:
        if(len(self.minHeap) > len(self.maxHeap)):
            return self.minHeap[0]
        if(len(self.maxHeap) > len(self.minHeap)):
            return self.maxHeap[0] * (-1)
        return (self.minHeap[0] + self.maxHeap[0] * (-1)) / 2

        