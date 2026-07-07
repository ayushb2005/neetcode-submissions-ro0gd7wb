class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        max heap with -1

        '''
        for i in range(len(stones)):
            stones[i] = stones[i]*(-1)
        heapq.heapify(stones)
        while(len(stones) != 0 and len(stones) != 1):
            y = -heapq.heappop(stones) 
            x = -heapq.heappop(stones)
            if(x<y):
                new = y-x
                heapq.heappush(stones,new * (-1))
        if not stones:
            return 0
        return stones[0] * (-1)
