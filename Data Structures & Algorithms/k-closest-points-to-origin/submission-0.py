class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        keep a max heap of k, if the length of it > k then just take off the farthest distance from the top
        '''
        heap = []
        for i in range(len(points)):
            p1 = points[i][0]
            p2 = points[i][1]
            distance = math.sqrt((p1-0)**2 + (p2-0)**2)
            heapq.heappush(heap, (-distance,points[i]))
            if(len(heap) > k):
                heapq.heappop(heap)
        heapReturn = []
        while(len(heap) != 0):
            heapReturn.append(heapq.heappop(heap)[1])
        return heapReturn
        
