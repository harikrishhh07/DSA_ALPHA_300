# Insertion Sort

<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />

<hr>

Given an array of integers `nums`, sort the array in ascending order using the **Insertion Sort algorithm**.

Insertion Sort builds the sorted portion of the array one element at a time. Starting from the second element, compare the current element with the elements before it. Shift all larger elements one position to the right and insert the current element into its correct position.

**Restriction:** Do not use `sort()`, `sorted()`, or `bisect.insort()`. Implement the shifting and insertion logic manually.

### Example 1:

**Input:** `nums = [5, 2, 4, 1, 3]`

**Output:** `[1, 2, 3, 4, 5]`

**Explanation:** Each element is inserted into its correct position in the sorted portion of the array.

### Example 2:

**Input:** `nums = [4, 3, 2, 1]`

**Output:** `[1, 2, 3, 4]`

**Explanation:** Each new element is smaller than the elements before it, so the algorithm shifts elements to the right before inserting it.

### Example 3:

**Input:** `nums = [1, 2, 3, 4, 5]`

**Output:** `[1, 2, 3, 4, 5]`

**Explanation:** The array is already sorted, so no shifting is required.

### Constraints:

- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`

### Expected Complexity:

- Best-case Time: `O(n)`
- Average-case Time: `O(n^2)`
- Worst-case Time: `O(n^2)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you implement Insertion Sort without creating another array?