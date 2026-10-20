# Sort Colors (Dutch National Flag Algorithm)

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given an array `nums` containing only `0`, `1`, and `2`, sort the array in ascending order.

The values represent three colors:

- `0` represents red.
- `1` represents white.
- `2` represents blue.

Rearrange the array so that all zeros appear first, followed by all ones and then all twos.

Solve the problem using the **Dutch National Flag algorithm**, which maintains three regions using the `low`, `mid`, and `high` pointers.

**Restriction:** Do not use `sort()`, `sorted()`, or any built-in sorting function. Perform the rearrangement manually using swaps and pointer updates.

### Example 1:

**Input:** `nums = [2, 0, 2, 1, 1, 0]`

**Output:** `[0, 0, 1, 1, 2, 2]`

**Explanation:** The algorithm moves zeros to the beginning, leaves ones in the middle, and moves twos to the end.

### Example 2:

**Input:** `nums = [2, 0, 1]`

**Output:** `[0, 1, 2]`

**Explanation:** The three pointers rearrange the elements in a single traversal.

### Example 3:

**Input:** `nums = [0, 1, 2, 0, 1, 2]`

**Output:** `[0, 0, 1, 1, 2, 2]`

**Explanation:** Each element is examined and placed into the correct region through pointer movement and swapping.

### Constraints:

- `1 <= nums.length <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

### Expected Complexity:

- Time: `O(n)`
- Auxiliary Space: `O(1)`

### Important Note:

When `nums[mid] == 2`, swap it with `nums[high]` and decrement `high`. Do not increment `mid` in this case, because the element swapped into the middle position has not yet been examined.

**Follow-up:** Can you sort the array in one pass without creating an additional array?