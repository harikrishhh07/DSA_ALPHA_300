# Find Rotation Count in Sorted Array

<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />

<hr>

Given an array of distinct integers originally sorted in ascending order and then rotated, determine the **number of rotations** performed.

A rotation moves the first element of the array to the end.

For an array that has been rotated, the rotation count equals the index of its minimum element.

Implement the solution using Binary Search.

**Restriction:** Do not use `bisect`, `min()`, `sort()`, or `sorted()`. Identify the minimum element using comparisons and return its index.

### Example 1:

**Input:** `nums = [4, 5, 1, 2, 3]`

**Output:** `2`

**Explanation:** The original array was `[1, 2, 3, 4, 5]`. Moving the first two elements to the end produces `[4, 5, 1, 2, 3]`. Therefore, the array was rotated twice.

### Example 2:

**Input:** `nums = [7, 9, 11, 12, 5]`

**Output:** `4`

**Explanation:** The minimum element `5` is at index `4`, so the array has been rotated four times.

### Example 3:

**Input:** `nums = [1, 2, 3, 4, 5]`

**Output:** `0`

**Explanation:** The array is already sorted in ascending order, so no rotation is needed.

### Example 4:

**Input:** `nums = [2, 1]`

**Output:** `1`

**Explanation:** Moving the first element of `[1, 2]` to the end produces `[2, 1]`. The minimum element is at index `1`.

### Constraints:

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- All elements are distinct.
- The array was originally sorted in ascending order.

### Expected Complexity:

- Best-case Time: `O(1)`
- Worst-case Time: `O(log n)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you determine the rotation count without repeatedly rotating the array or checking every element?

**Important Hint:** Find the index of the minimum element using Binary Search. That index gives the rotation count under the stated rotation convention.