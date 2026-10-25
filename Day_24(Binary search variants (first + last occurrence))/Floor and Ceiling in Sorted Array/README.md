# Floor and Ceiling in Sorted Array

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given an array of integers `nums` sorted in non-decreasing order and an integer `x`, find the **floor** and **ceiling** of `x` in the array.

- **Floor:** The greatest element in the array that is less than or equal to `x`.
- **Ceiling:** The smallest element in the array that is greater than or equal to `x`.

Return the result as `[floor, ceiling]`.

If the floor or ceiling does not exist, return `-1` for that value.

Implement the solution using Binary Search.

**Restriction:** Do not use `bisect_left()`, `bisect_right()`, `sort()`, or `sorted()`. Find both values manually using Binary Search.

### Example 1:

**Input:** `nums = [1, 2, 4, 6, 8, 10]`, `x = 5`

**Output:** `[4, 6]`

**Explanation:** The greatest element less than or equal to `5` is `4`, and the smallest element greater than or equal to `5` is `6`.

### Example 2:

**Input:** `nums = [1, 2, 4, 6, 8, 10]`, `x = 6`

**Output:** `[6, 6]`

**Explanation:** Since `6` exists in the array, both its floor and ceiling are `6`.

### Example 3:

**Input:** `nums = [3, 5, 7, 9]`, `x = 1`

**Output:** `[-1, 3]`

**Explanation:** No element is less than or equal to `1`, so the floor does not exist. The ceiling is `3`.

### Example 4:

**Input:** `nums = [3, 5, 7, 9]`, `x = 12`

**Output:** `[9, -1]`

**Explanation:** The floor is `9`, but no element is greater than or equal to `12`.

### Constraints:

- `1 <= nums.length <= 10^5`
- `0 <= nums[i], x <= 10^9`
- `nums` is sorted in non-decreasing order.

### Expected Complexity:

- Time: `O(log n)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you find both the floor and ceiling in a single Binary Search traversal?

**Important Hint:** If `nums[mid] < x`, update the floor candidate and move right. If `nums[mid] > x`, update the ceiling candidate and move left. If the values are equal, both floor and ceiling equal `x`.