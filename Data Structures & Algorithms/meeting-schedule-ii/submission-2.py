"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0
        
        current_max = res = 1

        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):

            if intervals[i - 1].start == intervals[i].start or intervals[i - 1].end > intervals[i].start:
                
                current_max += 1
            
            res = max(current_max, res)
        
        return res
            
