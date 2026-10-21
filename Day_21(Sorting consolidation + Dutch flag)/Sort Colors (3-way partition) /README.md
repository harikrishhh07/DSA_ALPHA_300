# Sort Colors (3-Way Partition)

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given an array of integers `nums` containing only `0`, `1`, and `2`, sort the array in ascending order using the **Dutch National Flag algorithm**.

The algorithm divides the array into three regions:

- `0`: Elements smaller than the pivot.
- `1`: Elements equal to the pivot.
- `2`: Elements greater than the pivot.

Use three pointers: `low`, `mid`, and `high` to rearrange the elements in a single traversal.

**Restriction:** Do not use `sort()` or `sorted()`. Implement the three-way partitioning, pointer updates, and swaps manually. You may reuse your own sorting functions from previous days.

### Example 1:

**Input:** `nums = [2, 0, 2, 1, 1, 0]`

**Output:** `[0, 0, 1, 1, 2, 2]`

**Explanation:** Move zeros to the beginning, keep ones in the middle, and move twos to the end.

### Example 2:

**Input:** `nums = [2, 0, 1]`

**Output:** `[0, 1, 2]`

**Explanation:** The three pointers rearrange the elements in a single traversal.

### Example 3:

**Input:** `nums = [0, 0, 1, 1, 2, 2]`

**Output:** `[0, 0, 1, 1, 2, 2]`

**Explanation:** The array is already sorted, so no effective swaps are required.

### Constraints:

- `1 <= nums.length <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

### Expected Complexity:

- Time: `O(n)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you solve this problem in one pass without creating an additional array?

**Important Note:** When `nums[mid] == 2`, swap it with `nums[high]` and decrement `high`. Do not increment `mid` until the swapped-in element has been examined.