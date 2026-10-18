# Sort Array with 3 Elements (0, 1, 2)

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given an array of integers `nums` containing only `0`, `1`, and `2`, sort the array in ascending order.

All occurrences of `0` must appear first, followed by all occurrences of `1`, and then all occurrences of `2`.

**Restriction:** Do not use `sort()`, `sorted()`, or any built-in sorting function. Rearrange the elements manually.

### Example 1:

**Input:** `nums = [2, 0, 2, 1, 1, 0]`

**Output:** `[0, 0, 1, 1, 2, 2]`

**Explanation:** Place all zeros before ones and all ones before twos.

### Example 2:

**Input:** `nums = [2, 0, 1]`

**Output:** `[0, 1, 2]`

**Explanation:** The three elements are rearranged into ascending order.

### Example 3:

**Input:** `nums = [0, 0, 1, 1, 2, 2]`

**Output:** `[0, 0, 1, 1, 2, 2]`

**Explanation:** The array is already sorted, so no rearrangement is required.

### Constraints:

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0`, `1`, or `2`.

### Expected Complexity:

- Time: `O(n)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you solve this problem in one pass using three pointers, without creating another array?