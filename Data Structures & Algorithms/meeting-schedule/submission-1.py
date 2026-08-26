"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if (intervals[j].start in range(intervals[i].start,intervals[i].end) or
                    intervals[j].end in range(intervals[i].start,intervals[i].end)):
                    return False
        
        return True

