class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        start = newInterval[0]
        end = newInterval[1]

        # Stage 1: Add intervals before the new interval
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # Stage 2: Merge overlapping intervals
        while i < n and intervals[i][0] <= end:
            if intervals[i][0] < start:
                start = intervals[i][0]

            if intervals[i][1] > end:
                end = intervals[i][1]

            i += 1

        result.append([start, end])

        # Stage 3: Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result