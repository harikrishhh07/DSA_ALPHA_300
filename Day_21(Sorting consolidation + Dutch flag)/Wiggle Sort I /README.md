# Wiggle Sort I

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given an integer array `nums`, reorder it in-place so that the elements follow the **wiggle pattern**:

`nums[0] <= nums[1] >= nums[2] <= nums[3] >= nums[4] ...`

In other words, every odd-indexed element must be greater than or equal to its adjacent even-indexed elements, while every even-indexed element after the first must be less than or equal to its adjacent odd-indexed elements.

If the current pair violates the required relationship, swap the two elements to restore the wiggle pattern.

**Restriction:** Do not use `sort()` or `sorted()`. Implement the rearrangement manually using comparisons and swaps.

### Example 1:

**Input:** `nums = [3, 5, 2, 1, 6, 4]`

**Output:** `[3, 5, 1, 6, 2, 4]`

**Explanation:** The resulting array satisfies `3 <= 5 >= 1 <= 6 >= 2 <= 4`.

### Example 2:

**Input:** `nums = [6, 6, 5, 6, 3, 8]`

**Output:** `[6, 6, 5, 6, 3, 8]`

**Explanation:** Equal adjacent values are allowed as long as the required wiggle inequalities hold.

### Example 3:

**Input:** `nums = [1, 2, 3, 4]`

**Output:** `[1, 3, 2, 4]`

**Explanation:** Swap adjacent elements when necessary to establish the alternating pattern.

### Constraints:

- `1 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] <= 10^4`
- A valid wiggle arrangement is guaranteed to exist.

### Expected Complexity:

- Time: `O(n)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you solve this problem in a single pass without sorting the array first?

**Hint:** At every odd index, ensure the current element is greater than or equal to the previous element. At every even index, ensure the current element is less than or equal to the previous element. Swap adjacent elements whenever the condition is violated.