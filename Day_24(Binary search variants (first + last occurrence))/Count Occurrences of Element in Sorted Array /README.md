# Count Occurrences of Element in Sorted Array

<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />

<hr>

Given an array of integers `nums` sorted in non-decreasing order and an integer `target`, return the **number of times the target occurs** in the array.

You must solve the problem using Binary Search rather than checking every element individually.

Find the first and last positions of the target and calculate the total number of occurrences.

**Restriction:** Do not use `bisect_left()`, `bisect_right()`, `count()`, or any built-in searching or counting function. Implement the first and last occurrence searches manually.

### Example 1:

**Input:** `nums = [1, 2, 2, 2, 3, 4]`, `target = 2`

**Output:** `3`

**Explanation:** The target `2` occurs at indices `1`, `2`, and `3`, giving a total count of `3`.

### Example 2:

**Input:** `nums = [1, 1, 2, 3, 3, 3, 3, 4]`, `target = 3`

**Output:** `4`

**Explanation:** The first occurrence of `3` is at index `3` and the last occurrence is at index `6`. The count is `6 - 3 + 1 = 4`.

### Example 3:

**Input:** `nums = [1, 2, 3, 4, 5]`, `target = 6`

**Output:** `0`

**Explanation:** The target is not present, so its frequency is zero.

### Example 4:

**Input:** `nums = [7, 7, 7, 7]`, `target = 7`

**Output:** `4`

**Explanation:** Every element equals the target.

### Constraints:

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i], target <= 10^9`
- `nums` is sorted in non-decreasing order.

### Expected Complexity:

- Time: `O(log n)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you reuse your first-occurrence and last-occurrence Binary Search functions from the previous problem?

**Important Hint:** If the target exists, the count is `last - first + 1`. Otherwise, return `0`.