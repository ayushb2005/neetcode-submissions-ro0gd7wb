class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        heap = []

        for i in points:
            distance = math.sqrt(i[0] * i[0] + i[1] * i[1])
            heapq.heappush(heap, (distance, i))
        returnArray = []
        counter = 0
        while heap and counter < k:
            pop = heapq.heappop(heap)
            returnArray.append(pop[1])
            counter += 1
        return returnArray
