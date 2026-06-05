class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        resultInterval = []
        intervals.sort()
        mergedInterval = None   
        for interval in intervals:
            if mergedInterval == None:
                mergedInterval = interval
            else:
                if(interval[0] > mergedInterval[1]):
                    resultInterval.append(mergedInterval)
                    mergedInterval = interval
                elif(mergedInterval[0] > interval[1]):
                    resultInterval.append(interval)
                else:
                    mergedInterval = [min(mergedInterval[0], interval[0]), max(mergedInterval[1], interval[1])]
        resultInterval.append(mergedInterval)
        return resultInterval