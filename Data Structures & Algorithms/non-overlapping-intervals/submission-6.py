class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        interval = None
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        counter = 0 
        for i in range(len(intervals)):
            if interval is None:
                interval = intervals[i]
            else:
                if(interval[1] <= intervals[i][0]):
                    interval = intervals[i]
                else:
                    
                    counter += 1
        return counter