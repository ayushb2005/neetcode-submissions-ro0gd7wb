class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        compare interval if they collide 
        first check overlap
        '''
        outputArray = []
        for i in range(len(intervals)):
            if(newInterval[1] < intervals[i][0]):
                outputArray.append(newInterval)
                return outputArray + intervals[i:]
            elif(newInterval[0] > intervals[i][1]):
                outputArray.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]),\
                max(intervals[i][1], newInterval[1])]
        outputArray.append(newInterval)
        return outputArray
            


