class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        intervals = merge_sort_intervals(intervals, 1)

        kept = 1
        last_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start >= last_end:
                kept += 1
                last_end = end

        return len(intervals) - kept