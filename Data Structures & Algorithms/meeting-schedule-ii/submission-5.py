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

        new_intervals = []

        for i in range(len(intervals)):
            new_intervals.append([intervals[i].start, "s"])
            new_intervals.append([intervals[i].end, "e"])
        
        new_intervals.sort(key=lambda x: (x[0], x[1] != "e"))

        active_intervals = 0
        res = 0

        for i in range(len(new_intervals)):

            if new_intervals[i][1] == "s":
                active_intervals += 1
            else:
                active_intervals -= 1
        
            res = max(active_intervals, res)
        return res
            
