class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        interval = None
        intervals.sort()
        returnArray = []
        for i in range(len(intervals)):
            if(interval == None):
                interval = intervals[i]
            else:
                if(interval[1] < intervals[i][0]):
                    returnArray.append(interval)
                    interval = intervals[i]
                else:
                    interval = [min(interval[0], intervals[i][0]), \
                    max(interval[1], intervals[i][1])]
        
        returnArray.append(interval)
        return returnArray