class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()


        overlap = 0

        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                overlap += 1
                prev_end = min(intervals[i][1], prev_end)
            else:
                prev_end = intervals[i][1]
        
        return overlap


        