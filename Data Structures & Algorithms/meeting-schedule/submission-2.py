"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortedMeetings = []
        for i in intervals:
            sortedMeetings.append((i.start, i.end))
        sortedMeetings.sort()
        print(sortedMeetings)
        prev = None
        for i in sortedMeetings:
            if prev is None:
                prev = i
            else:
                if(prev[1] <= i[0]):
                    prev = i
                    continue
                else:
                    return False
        return True