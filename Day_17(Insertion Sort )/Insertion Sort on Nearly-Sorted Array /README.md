# Insertion Sort on Nearly-Sorted Array

<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />

<hr>

Given an array of integers `nums` that is **nearly sorted**, sort the array in ascending order using the **Insertion Sort algorithm**.

A nearly sorted array is an array in which each element is already close to its correct sorted position. In many such cases, only a small number of shifts are required to complete the sorting.

Start from the second element, store it as the `key`, shift larger elements to the right, and insert the key into its correct position.

**Restriction:** Do not use `sort()`, `sorted()`, `bisect.insort()`, or any built-in sorting function. Implement the insertion and shifting logic manually.

### Example 1:

**Input:** `nums = [1, 2, 4, 3, 5, 6]`

**Output:** `[1, 2, 3, 4, 5, 6]`

**Explanation:** Only the elements `4` and `3` are out of order. Insertion Sort shifts `4` one position to the right and inserts `3` before it.

### Example 2:

**Input:** `nums = [2, 1, 3, 5, 4]`

**Output:** `[1, 2, 3, 4, 5]`

**Explanation:** The elements `2` and `1`, as well as `5` and `4`, need to be reordered.

### Example 3:

**Input:** `nums = [1, 2, 3, 4, 5]`

**Output:** `[1, 2, 3, 4, 5]`

**Explanation:** The array is already sorted. Insertion Sort completes the process with no shifts.

### Constraints:

- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- The array may already be sorted or may contain a small number of misplaced elements.

### Expected Complexity:

- Best-case Time: `O(n)`
- Average-case Time: `O(n^2)`
- Worst-case Time: `O(n^2)`
- Auxiliary Space: `O(1)`

**Follow-up:** Why does Insertion Sort often perform well on nearly sorted arrays compared with its worst-case performance?