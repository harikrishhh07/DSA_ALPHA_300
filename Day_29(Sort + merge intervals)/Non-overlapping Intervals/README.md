# Non-overlapping Intervals

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

You are given an array of intervals, where `intervals[i] = [start_i, end_i]`.

Return the **minimum number of intervals you must remove** so that the remaining intervals are non-overlapping.

Two intervals that share an endpoint are considered non-overlapping. For example, `[1,2]` and `[2,3]` can both remain.

**Restriction:** Do not use `.sort()` or `sorted()`. Implement your own Merge Sort or Quick Sort to arrange the intervals by their ending points or starting points. Then determine which intervals can remain without overlapping.

### Example 1:
**Input:** `intervals = [[1,2],[2,3],[3,4],[1,3]]`

**Output:** `1`

**Explanation:** Remove `[1,3]`. The remaining intervals `[1,2]`, `[2,3]`, and `[3,4]` are non-overlapping. Only one removal is required.

### Example 2:
**Input:** `intervals = [[1,2],[1,2],[1,2]]`

**Output:** `2`

**Explanation:** All three intervals overlap. You can keep one interval and remove the other two.

### Example 3:
**Input:** `intervals = [[1,2],[2,3]]`

**Output:** `0`

**Explanation:** The intervals share an endpoint but do not overlap according to the problem's definition. No removal is needed.

### Constraints:
- `1 <= len(intervals) <= 10^5`
- `intervals[i].length == 2`
- `-5 * 10^4 <= start_i < end_i <= 5 * 10^4`

### Expected Complexity:
- **Time:** `O(n log n)` for sorting and `O(n)` for selecting intervals.
- **Auxiliary Space:** `O(n)` for a Merge Sort implementation, excluding the output or selection result.

**Follow-up:** Can you minimize removals by selecting intervals in increasing order of their ending points? Explain why choosing an interval that finishes earlier can leave more room for future intervals.