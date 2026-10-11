class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])

        merged_intervals = []

        for i in range(0, 1):
            merged_intervals.append(intervals[i])

        for i in range(1, len(intervals)):
            current_start = merged_intervals[-1][0]
            current_end = merged_intervals[-1][1]

            # if i >= len(intervals):
            #     continue

            next_start, next_end = intervals[i][0], intervals[i][1]

            if current_start == next_start or current_end >= next_start:
                merged_intervals[-1][0] = min(current_start, next_start)
                merged_intervals[-1][1] = max(current_end, next_end)
            else:
                merged_intervals.append(intervals[i])
        
        return merged_intervals
            