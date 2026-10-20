# Sort an Array of 0s and 1s

<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />

<hr>

Given an array of binary integers `nums`, containing only `0` and `1`, sort the array in ascending order.

All zeros must appear before all ones.

Implement the solution manually without using built-in sorting functions. You may use a counting-based approach or a two-pointer approach.

**Restriction:** Do not use `sort()`, `sorted()`, or `collections.Counter`. Count or rearrange the elements using loops and basic variables.

### Example 1:

**Input:** `nums = [0, 1, 0, 1, 1, 0]`

**Output:** `[0, 0, 0, 1, 1, 1]`

**Explanation:** The array contains three zeros and three ones. Place all zeros before all ones.

### Example 2:

**Input:** `nums = [1, 1, 1, 0, 0]`

**Output:** `[0, 0, 1, 1, 1]`

**Explanation:** The two zeros are moved to the beginning, followed by the three ones.

### Example 3:

**Input:** `nums = [0, 0, 0, 0]`

**Output:** `[0, 0, 0, 0]`

**Explanation:** The array already satisfies the required order.

### Example 4:

**Input:** `nums = [1, 1, 1, 1]`

**Output:** `[1, 1, 1, 1]`

**Explanation:** Since every element is `1`, no rearrangement is needed.

### Constraints:

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

### Expected Complexity:

- Time: `O(n)`
- Auxiliary Space: `O(1)` for an in-place two-pointer or counting-and-overwrite approach.

**Follow-up:** Can you solve this problem in one pass using two pointers, without counting the zeros first?