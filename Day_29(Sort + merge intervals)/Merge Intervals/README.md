# Merge Intervals

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

You are given an array of intervals, where `intervals[i] = [start_i, end_i]` represents the starting and ending points of an interval.

Merge all overlapping intervals and return an array containing only the non-overlapping intervals that cover the same ranges as the original intervals.

Two intervals overlap when the start of the next interval is less than or equal to the end of the current interval.

**Restriction:** Do not use `.sort()` or `sorted()`. Implement your own Merge Sort or Quick Sort to arrange the intervals by their starting points before merging them.

### Example 1:
**Input:** `intervals = [[1,3],[2,6],[8,10],[15,18]]`

**Output:** `[[1,6],[8,10],[15,18]]`

**Explanation:**
- `[1,3]` and `[2,6]` overlap, so they merge into `[1,6]`.
- `[8,10]` does not overlap with `[1,6]`.
- `[15,18]` does not overlap with `[8,10]`.

The final result contains three non-overlapping intervals.

### Example 2:
**Input:** `intervals = [[1,4],[4,5]]`

**Output:** `[[1,5]]`

**Explanation:** The intervals share the endpoint `4`, so they merge into `[1,5]`.

### Example 3:
**Input:** `intervals = [[4,7],[1,4]]`

**Output:** `[[1,7]]`

**Explanation:** After arranging the intervals by starting point, `[1,4]` and `[4,7]` merge into `[1,7]`.

### Constraints:
- `1 <= len(intervals) <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

### Expected Complexity:
- **Time:** `O(n log n)` for sorting and merging.
- **Auxiliary Space:** `O(n)` for a Merge Sort implementation, excluding the output array.

**Follow-up:** Can you merge the intervals in a single linear pass after sorting? Explain why sorting by starting point makes the merging process easier.