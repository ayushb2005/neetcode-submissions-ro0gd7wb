class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        returnArray = []

        for interval in range(len(intervals)):
            if(newInterval[0] > intervals[interval][1]):
                returnArray.append(intervals[interval])
            elif(newInterval[1] < intervals[interval][0]):
                returnArray.append(newInterval)
                returnArray.extend(intervals[interval:])
                return returnArray
            else:
                newInterval = [min(newInterval[0], intervals[interval][0]), \
                max(newInterval[1],intervals[interval][1])]
        returnArray.append(newInterval)
        return returnArray