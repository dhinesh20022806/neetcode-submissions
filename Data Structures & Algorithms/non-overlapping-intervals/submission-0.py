class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()


        overlap = 0

        current_end = intervals[0][1]

        for i in range(1, len(intervals)):

            if current_end > intervals[i][0]:
                overlap += 1
                current_end = min(intervals[i][1], current_end)
            else:
                curent_end = intervals[i][1]
        
        return overlap


        