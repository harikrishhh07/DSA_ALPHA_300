# Search in Rotated Sorted Array

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given an integer array `nums` sorted in ascending order with distinct elements, the array is rotated at an unknown pivot. Given an integer `target`, return its index if it exists in the array. Otherwise, return `-1`.

A rotated sorted array is created by moving some elements from the beginning of a sorted array to its end.

Implement the solution using **Binary Search** in `O(log n)` time.

**Restriction:** Do not use `bisect`, `bisect_left()`, `bisect_right()`, or any built-in searching function. Identify which half is sorted and determine whether the target belongs in that half.

### Example 1:

**Input:** `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`

**Output:** `4`

**Explanation:** The left half `[4, 5, 6, 7]` is sorted, but the target is not in that half. Search the right half to find `0` at index `4`.

### Example 2:

**Input:** `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 3`

**Output:** `-1`

**Explanation:** The target `3` does not exist in the array.

### Example 3:

**Input:** `nums = [1]`, `target = 0`

**Output:** `-1`

**Explanation:** The array contains only one element, and it does not match the target.

### Example 4:

**Input:** `nums = [6, 7, 1, 2, 3, 4, 5]`, `target = 3`

**Output:** `4`

**Explanation:** The middle element helps identify the sorted half. Repeatedly eliminate the half that cannot contain the target until index `4` is found.

### Constraints:

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All elements of `nums` are unique.
- `nums` is originally sorted in ascending order and then rotated.
- `-10^4 <= target <= 10^4`

### Expected Complexity:

- Best-case Time: `O(1)`
- Average-case Time: `O(log n)`
- Worst-case Time: `O(log n)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you solve this problem using a single Binary Search loop without first finding the rotation pivot?

**Important Hint:** If `nums[low] <= nums[mid]`, the left half is sorted. Otherwise, the right half is sorted. Check whether the target falls within the sorted half's range before updating the search boundaries.