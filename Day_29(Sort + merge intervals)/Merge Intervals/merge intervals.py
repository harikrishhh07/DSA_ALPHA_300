class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        intervals = merge_sort_intervals(intervals, 0)

        result = [intervals[0][:]]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            last_end = result[-1][1]

            if start <= last_end:
                if end > last_end:
                    result[-1][1] = end
            else:
                result.append([start, end])

        return result