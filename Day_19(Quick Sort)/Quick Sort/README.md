# Quick Sort

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given an array of integers `nums`, sort the array in ascending order using the **Quick Sort algorithm**.

Quick Sort is a divide-and-conquer algorithm that selects a pivot element and partitions the array so that smaller elements appear on one side of the pivot and larger elements appear on the other side. It then recursively sorts the resulting subarrays.

Implement Quick Sort from scratch using a partitioning algorithm such as **Lomuto partition** or **Hoare partition**.

**Restriction:** Do not use `sort()` or `sorted()`. Implement the partitioning, swapping, and recursive sorting operations manually.

### Example 1:

**Input:** `nums = [10, 7, 8, 9, 1, 5]`

**Output:** `[1, 5, 7, 8, 9, 10]`

**Explanation:** The algorithm selects a pivot, partitions the array around it, and recursively sorts the remaining subarrays.

### Example 2:

**Input:** `nums = [4, 2, 6, 1, 3]`

**Output:** `[1, 2, 3, 4, 6]`

**Explanation:** Partitioning places smaller elements before larger elements until the entire array is sorted.

### Example 3:

**Input:** `nums = [3, 3, 3, 3]`

**Output:** `[3, 3, 3, 3]`

**Explanation:** All elements are equal, so the final array remains unchanged.

### Constraints:

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

### Expected Complexity:

- Best-case Time: `O(n log n)`
- Average-case Time: `O(n log n)`
- Worst-case Time: `O(n^2)`
- Auxiliary Space: `O(log n)` on average for recursion; `O(n)` in the worst case.

**Follow-up:** Implement both Lomuto and Hoare partition schemes. How does pivot selection affect Quick Sort's performance?