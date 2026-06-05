"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        previousInterval = None
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            if previousInterval is None:
                previousInterval = interval
            else:
                if(previousInterval.end > interval.start):
                    return False
                else:
                    previousInterval = interval
        return True