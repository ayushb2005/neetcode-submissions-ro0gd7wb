class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[0])

        for i in range(len(queries)):
            queries[i] = (queries[i], i)
        queries.sort()
        
        minHeap = []
        outputArray = [-1]*len(queries)
        
        qp = 0
        ip = 0

        while(qp < len(queries)):
            while(ip < len(intervals) and queries[qp][0] >= intervals[ip][0]):
                length = intervals[ip][1] - intervals[ip][0] + 1
                heapq.heappush(minHeap, (length, intervals[ip][1]))
                ip += 1
            while(minHeap and queries[qp][0] > minHeap[0][1]):
                heapq.heappop(minHeap)
            if minHeap: 
                outputArray[queries[qp][1]] = minHeap[0][0]
            qp += 1
        return outputArray
        

                


        