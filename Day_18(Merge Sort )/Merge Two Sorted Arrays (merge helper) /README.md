# Merge Two Sorted Arrays

<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />

<hr>

Given two arrays of integers, `nums1` and `nums2`, both sorted in ascending order, merge them into a single array sorted in ascending order.

Implement a **merge helper** that compares the current elements of both arrays and adds the smaller element to the result. When one array is exhausted, append the remaining elements from the other array.

**Restriction:** Do not use `sort()`, `sorted()`, or `heapq.merge()`. Implement the merging logic manually using pointers.

### Example 1:

**Input:** `nums1 = [1, 3, 5]`, `nums2 = [2, 4, 6]`

**Output:** `[1, 2, 3, 4, 5, 6]`

**Explanation:** Compare the first available element from each array, repeatedly choose the smaller one, and append any remaining elements.

### Example 2:

**Input:** `nums1 = [1, 2, 3]`, `nums2 = [4, 5, 6]`

**Output:** `[1, 2, 3, 4, 5, 6]`

**Explanation:** All elements of `nums1` are smaller than those of `nums2`, so the two arrays are combined in order.

### Example 3:

**Input:** `nums1 = [1, 4, 7]`, `nums2 = [2, 3, 8, 9]`

**Output:** `[1, 2, 3, 4, 7, 8, 9]`

**Explanation:** The pointers move through both arrays, selecting the smaller available value at each step.

### Constraints:

- `0 <= nums1.length, nums2.length <= 10^5`
- `-10^9 <= nums1[i], nums2[i] <= 10^9`
- Both input arrays are sorted in ascending order.

### Expected Complexity:

Let `n` be the length of `nums1` and `m` be the length of `nums2`.

- Time: `O(n + m)`
- Auxiliary Space: `O(n + m)` for the merged result.

**Follow-up:** Can you use the same merge helper as part of your Merge Sort implementation?