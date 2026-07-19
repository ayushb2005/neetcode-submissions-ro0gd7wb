"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        heapSize = 0
        maxHeap = 0
        heap = []
        for i in intervals:
            if not heap:
                heapq.heappush(heap, i.end)
                heapSize += 1
            else:
                if(i.start >= heap[0]):
                    heapq.heappop(heap)
                    heapq.heappush(heap, i.end)
                else:
                    heapq.heappush(heap, i.end)
                    heapSize += 1
            maxHeap = max(heapSize, maxHeap)
        return maxHeap
        
        

        return 0