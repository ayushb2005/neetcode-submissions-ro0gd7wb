class MedianFinder:
    # import heapq
    def __init__(self):
        self.small, self.large = [], []
    def addNum(self, num: int) -> None:
        '''
        min heap for larger array values
        max heap for smaller array values
        when getting median i can either see if one is > than other
        if so take from bigger array otherwise just take the max from < array
        and min from > array
        need to move elements if size becomes > 1,
        always append to smaller heap, then append to larger heap
        check when adding to max heap that it is smaller than the min heap
        '''
        heapq.heappush(self.small, -1 * num)
        # 4 3 
        if(self.small and self.large and (-1) * self.small[0] > self.large[0]):
            poppedMax = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, poppedMax)
        if(len(self.small) > len(self.large) + 1):
            poppedMax = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, poppedMax)
        if(len(self.large) > len(self.small) + 1):
            poppedMin = heapq.heappop(self.large)
            heapq.heappush(self.small, poppedMin*(-1))
        
    def findMedian(self) -> float:
        if(len(self.small) == len(self.large)):
            return (-1*self.small[0] + self.large[0])/2
        else:
            if(len(self.large) > len(self.small)):
                return self.large[0]
            else:
                return -1*self.small[0]
        