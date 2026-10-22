# Binary Search

<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />

<hr>

Given an array of integers `nums` sorted in ascending order and an integer `target`, return the index of `target` if it exists in the array. Otherwise, return `-1`.

Implement the **Binary Search algorithm** by repeatedly dividing the search interval into two halves.

At each step:
1. Calculate the middle index.
2. If the middle element equals `target`, return its index.
3. If the middle element is smaller than `target`, search the right half.
4. Otherwise, search the left half.

**Restriction:** Do not use `bisect`, `bisect_left()`, or `bisect_right()`. Implement the search manually using `low`, `high`, and `mid` pointers. Calculate the midpoint using `low + (high - low) // 2`.

### Example 1:

**Input:** `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`

**Output:** `4`

**Explanation:** The middle element is `3`. Since `3 < 9`, search the right half. The next midpoint is `9`, which is found at index `4`.

### Example 2:

**Input:** `nums = [-1, 0, 3, 5, 9, 12]`, `target = 2`

**Output:** `-1`

**Explanation:** The search interval keeps shrinking until no candidate indices remain. Since `2` is absent, return `-1`.

### Example 3:

**Input:** `nums = [5]`, `target = 5`

**Output:** `0`

**Explanation:** The array contains only one element, and it matches the target.

### Constraints:

- `1 <= nums.length <= 10^4`
- All elements in `nums` are unique.
- `-10^4 <= nums[i], target <= 10^4`
- `nums` is sorted in ascending order.

### Expected Complexity:

- Best-case Time: `O(1)`
- Average-case Time: `O(log n)`
- Worst-case Time: `O(log n)`
- Auxiliary Space: `O(1)` for the iterative implementation.

**Follow-up:** Can you implement Binary Search iteratively without using recursion or any built-in searching functions?