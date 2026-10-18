# Merge Sort

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given an array of integers `nums`, sort the array in ascending order using the **Merge Sort algorithm**.

Merge Sort is a divide-and-conquer algorithm that divides the array into smaller subarrays, recursively sorts each subarray, and merges the sorted subarrays to produce the final sorted array.

Your implementation must contain two main operations:

1. **Divide:** Split the array into two halves until each subarray contains one element.
2. **Merge:** Combine the sorted halves by comparing their elements and placing them in the correct order.

**Restriction:** Do not use `sort()`, `sorted()`, or `heapq.merge()`. Implement the recursive splitting and merging operations manually.

### Example 1:

**Input:** `nums = [38, 27, 43, 3, 9, 82, 10]`

**Output:** `[3, 9, 10, 27, 38, 43, 82]`

**Explanation:** The array is recursively divided into smaller subarrays. The subarrays are then merged in sorted order until the complete array is sorted.

### Example 2:

**Input:** `nums = [5, 2, 8, 1, 3]`

**Output:** `[1, 2, 3, 5, 8]`

**Explanation:** The array is divided into smaller parts, sorted recursively, and merged to obtain the final result.

### Example 3:

**Input:** `nums = [1, 2, 3, 4]`

**Output:** `[1, 2, 3, 4]`

**Explanation:** Even though the array is already sorted, the standard Merge Sort algorithm still performs its recursive splitting and merging operations.

### Constraints:

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

### Expected Complexity:

- Best-case Time: `O(n log n)`
- Average-case Time: `O(n log n)`
- Worst-case Time: `O(n log n)`
- Auxiliary Space: `O(n)` for the temporary arrays used during merging, excluding recursion-stack space.

**Follow-up:** Why does Merge Sort guarantee `O(n log n)` time even when the input array is sorted in reverse order?