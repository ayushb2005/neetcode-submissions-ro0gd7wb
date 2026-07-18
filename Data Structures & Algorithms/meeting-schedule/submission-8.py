"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: (x.start))
        print(intervals)
        interval = None
        for i in range(len(intervals)):
            if interval is None:
                interval = intervals[i]
            else:
                if(interval.end > intervals[i].start):
                    return False
                else:
                    interval = intervals[i]
        return True