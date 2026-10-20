# Quick Sort with 3-Way Partition

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given an array of integers `nums`, sort the array in ascending order using **Quick Sort with 3-way partitioning**.

Unlike standard Quick Sort, which divides the array into elements smaller and larger than the pivot, 3-way partitioning divides it into three regions:

1. Elements smaller than the pivot.
2. Elements equal to the pivot.
3. Elements greater than the pivot.

Recursively sort only the regions containing elements smaller than or greater than the pivot. The equal region is already in its correct position.

**Restriction:** Do not use `sort()` or `sorted()`. Implement the partitioning and swapping logic manually.

### Example 1:

**Input:** `nums = [3, 5, 2, 3, 8, 3, 1, 5]`

**Output:** `[1, 2, 3, 3, 3, 5, 5, 8]`

**Explanation:** All occurrences of the pivot value `3` are grouped together during partitioning, reducing unnecessary recursive work.

### Example 2:

**Input:** `nums = [4, 4, 4, 4, 4]`

**Output:** `[4, 4, 4, 4, 4]`

**Explanation:** All elements are equal. A single 3-way partition identifies the equal region, avoiding repeated unbalanced partitions.

### Example 3:

**Input:** `nums = [9, 1, 7, 1, 3, 9, 2]`

**Output:** `[1, 1, 2, 3, 7, 9, 9]`

**Explanation:** The algorithm groups duplicate values and recursively sorts the regions on either side of the equal region.

### Constraints:

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

### Expected Complexity:

- Best-case Time: `O(n)`
- Average-case Time: `O(n log n)`
- Worst-case Time: `O(n^2)` with consistently poor pivot choices.
- Auxiliary Space: `O(log n)` on average for recursion; `O(n)` in the worst case.

**Follow-up:** Why does 3-way partitioning often outperform standard Quick Sort when the array contains many duplicate elements?