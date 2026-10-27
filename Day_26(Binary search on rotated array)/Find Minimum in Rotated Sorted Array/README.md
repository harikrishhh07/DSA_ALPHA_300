# Find Minimum in Rotated Sorted Array

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given an array of `n` integers that was originally sorted in ascending order and then rotated between `1` and `n` times, find and return the **minimum element**.

All elements in the array are distinct.

Implement the solution using Binary Search with `O(log n)` time complexity.

**Restriction:** Do not use `bisect`, `min()`, `sort()`, or `sorted()`. Determine the minimum by comparing the middle element with the rightmost element in the current search interval.

### Example 1:

**Input:** `nums = [3, 4, 5, 1, 2]`

**Output:** `1`

**Explanation:** The original sorted array was `[1, 2, 3, 4, 5]`. After rotation, the minimum element `1` appears at index `3`.

### Example 2:

**Input:** `nums = [4, 5, 6, 7, 0, 1, 2]`

**Output:** `0`

**Explanation:** The minimum element is `0`, located at index `4`.

### Example 3:

**Input:** `nums = [11, 13, 15, 17]`

**Output:** `11`

**Explanation:** The array is sorted without a rotation that changes its order. The first element is the minimum.

### Example 4:

**Input:** `nums = [2, 1]`

**Output:** `1`

**Explanation:** Comparing the two elements identifies `1` as the minimum.

### Constraints:

- `1 <= nums.length <= 5000`
- `-5000 <= nums[i] <= 5000`
- All elements are unique.
- The array was originally sorted in ascending order and then rotated.

### Expected Complexity:

- Best-case Time: `O(1)`
- Worst-case Time: `O(log n)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you find the minimum without locating the rotation pivot separately?

**Important Hint:** Compare `nums[mid]` with `nums[high]`.

- If `nums[mid] > nums[high]`, the minimum must be to the right of `mid`.
- Otherwise, the minimum lies at `mid` or to its left.

Continue until `low == high`. The element at that index is the minimum.