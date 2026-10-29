# Insert Interval

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

You are given an array of non-overlapping intervals `intervals`, sorted in ascending order by their starting points, and a new interval `newInterval = [start, end]`.

Insert the new interval into the existing intervals and merge any overlapping intervals. Return the resulting array of non-overlapping intervals in ascending order.

The original intervals are already sorted and non-overlapping, so you should preserve their order and avoid unnecessary re-sorting.

**Restriction:** Do not use `.sort()`, `sorted()`, or `bisect`. Process the existing intervals directly, merging overlapping intervals with `newInterval` when necessary.

### Example 1:
**Input:** `intervals = [[1,3],[6,9]], newInterval = [2,5]`

**Output:** `[[1,5],[6,9]]`

**Explanation:** The new interval `[2,5]` overlaps with `[1,3]`, so they merge into `[1,5]`. The interval `[6,9]` remains unchanged.

### Example 2:
**Input:** `intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]`

**Output:** `[[1,2],[3,10],[12,16]]`

**Explanation:**
- `[1,2]` remains unchanged because it comes before the new interval.
- `[3,5]`, `[6,7]`, and `[8,10]` overlap with the expanding new interval.
- These overlapping intervals merge into `[3,10]`.
- `[12,16]` remains unchanged.

### Example 3:
**Input:** `intervals = [], newInterval = [5,7]`

**Output:** `[[5,7]]`

**Explanation:** Since there are no existing intervals, the result contains only the new interval.

### Constraints:
- `0 <= len(intervals) <= 10^4`
- `intervals[i].length == 2`
- `newInterval.length == 2`
- `0 <= start_i <= end_i <= 10^5`
- The original intervals are sorted by starting point and do not overlap.

### Expected Complexity:
- **Time:** `O(n)`, where `n` is the number of existing intervals.
- **Auxiliary Space:** `O(n)` for the resulting interval list.

**Follow-up:** Solve this problem in one pass without sorting. Divide the process into three stages: intervals before the new interval, overlapping intervals, and intervals after the new interval.