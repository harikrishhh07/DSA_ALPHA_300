# Find First and Last Position in Sorted Array

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given an array of integers `nums` sorted in non-decreasing order, find the **starting and ending positions** of a given `target`.

If the target is not found in the array, return `[-1, -1]`.

You must implement an algorithm with `O(log n)` time complexity.

Use two modified Binary Search operations:

1. Find the first occurrence of the target.
2. Find the last occurrence of the target.

**Restriction:** Do not use `bisect_left()`, `bisect_right()`, `index()`, or built-in searching functions. Implement both Binary Search variants manually.

### Example 1:

**Input:** `nums = [5, 7, 7, 8, 8, 10]`, `target = 8`

**Output:** `[3, 4]`

**Explanation:** The target `8` first appears at index `3` and last appears at index `4`.

### Example 2:

**Input:** `nums = [5, 7, 7, 8, 8, 10]`, `target = 6`

**Output:** `[-1, -1]`

**Explanation:** The target `6` does not appear in the array.

### Example 3:

**Input:** `nums = []`, `target = 0`

**Output:** `[-1, -1]`

**Explanation:** The array is empty, so the target cannot be found.

### Example 4:

**Input:** `nums = [2, 2, 2, 2, 2]`, `target = 2`

**Output:** `[0, 4]`

**Explanation:** The target occurs at every index, so the first position is `0` and the last position is `4`.

### Constraints:

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i], target <= 10^9`
- `nums` is sorted in non-decreasing order.

### Expected Complexity:

- Time: `O(log n)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you find both boundaries using two independent Binary Search passes instead of scanning outward from one occurrence?

**Important Hint:** When the target is found, continue searching left to find the first occurrence and right to find the last occurrence.