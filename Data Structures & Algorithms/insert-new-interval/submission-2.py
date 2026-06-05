class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        resultInterval = []

        for interval in intervals:
            if(newInterval[0] > interval[1]):
                resultInterval.append(interval)
            elif(newInterval[1] < interval[0]):
                resultInterval.append(newInterval)
                newInterval = interval
            else:
                newInterval = [min(newInterval[0],interval[0]), max(newInterval[1],interval[1])]
        resultInterval.append(newInterval)
        return resultInterval