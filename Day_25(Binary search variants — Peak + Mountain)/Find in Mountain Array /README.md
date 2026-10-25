# Find in Mountain Array

<img src="https://img.shields.io/badge/Difficulty-Hard-red" alt="Difficulty: Hard" />

<hr>

You are given a **mountain array** and an integer `target`.

A mountain array is an array that strictly increases to a peak element and then strictly decreases.

Your task is to find the **minimum index** at which `target` occurs in the mountain array.

If the target does not exist, return `-1`.

You cannot access the array directly. Instead, you are provided with a `MountainArray` interface containing two methods:

- `MountainArray.get(index)` — returns the element at the specified index.
- `MountainArray.length()` — returns the length of the mountain array.

Implement the function `findInMountainArray(target, mountain_arr)` using Binary Search.

Your solution should use the following approach:

1. Find the peak index using Binary Search.
2. Search for the target in the increasing portion.
3. If the target is not found, search the decreasing portion using modified Binary Search.

**Restriction:** Do not use `bisect`, `index()`, `max()`, or any built-in searching function. Implement all Binary Search operations manually. You must not make more than `100` calls to `MountainArray.get()`.

### Example 1:

**Input:** `mountainArr = [1, 2, 3, 4, 5, 3, 1]`, `target = 3`

**Output:** `2`

**Explanation:** The target `3` occurs at indices `2` and `5`. Since the problem requires the minimum index, return `2`.

### Example 2:

**Input:** `mountainArr = [0, 1, 2, 4, 2, 1]`, `target = 3`

**Output:** `-1`

**Explanation:** The target `3` is not present in either the increasing or decreasing portion of the mountain array.

### Example 3:

**Input:** `mountainArr = [1, 5, 9, 12, 8, 4, 2]`, `target = 8`

**Output:** `4`

**Explanation:** The peak element is `12` at index `3`. The target `8` is found in the decreasing portion at index `4`.

### Example 4:

**Input:** `mountainArr = [1, 3, 7, 10, 6, 2]`, `target = 10`

**Output:** `3`

**Explanation:** The target is the peak element itself, located at index `3`.

### Constraints:

- `3 <= mountain_arr.length() <= 10^4`
- `0 <= target <= 10^9`
- `0 <= mountain_arr.get(index) <= 10^9`
- The array is guaranteed to be a valid mountain array.
- At most `100` calls to `MountainArray.get()` are allowed.

### Expected Complexity:

- Time: `O(log n)`
- Auxiliary Space: `O(1)` for an iterative implementation.

### Important Hint:

First find the peak using the condition:

`mountain_arr.get(mid) < mountain_arr.get(mid + 1)`

Then perform two separate searches:

- **Ascending Binary Search:** If `mid_value < target`, move right.
- **Descending Binary Search:** If `mid_value < target`, move left.

Always search the increasing portion first to ensure that the smallest valid index is returned.

**Follow-up:** Can you minimize API calls by storing previously retrieved values instead of repeatedly calling `MountainArray.get()` for the same index?