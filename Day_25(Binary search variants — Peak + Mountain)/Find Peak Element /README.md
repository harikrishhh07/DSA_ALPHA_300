# Find Peak Element

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given an integer array `nums`, find a **peak element** and return its index.

A peak element is an element that is strictly greater than its neighboring elements.

For the first and last elements, imagine that the elements outside the array have values of negative infinity.

You may assume that `nums[-1] = nums[n] = -infinity`.

If the array contains multiple peak elements, return the index of **any one of them**.

Your solution must run in `O(log n)` time.

**Restriction:** Do not use `bisect`, `max()`, `index()`, or any built-in searching function. Implement Binary Search manually by comparing adjacent elements.

### Example 1:

**Input:** `nums = [1, 2, 3, 1]`

**Output:** `2`

**Explanation:** The element `3` is greater than both its neighbors, `2` and `1`. Therefore, index `2` is a peak.

### Example 2:

**Input:** `nums = [1, 2, 1, 3, 5, 6, 4]`

**Output:** `5`

**Explanation:** The element `6` is greater than its neighbors, `5` and `4`. Index `2` is also a valid answer because the element `1` at that index is not a peak, but index `1` is a peak with value `2`.

### Example 3:

**Input:** `nums = [1]`

**Output:** `0`

**Explanation:** A single element is considered a peak because its imaginary neighbors are negative infinity.

### Example 4:

**Input:** `nums = [5, 4, 3, 2, 1]`

**Output:** `0`

**Explanation:** The first element `5` is greater than its right neighbor, so index `0` is a peak.

### Constraints:

- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid adjacent indices.

### Expected Complexity:

- Time: `O(log n)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you find a peak without scanning every element?

**Important Hint:** Compare `nums[mid]` with `nums[mid + 1]`.

- If `nums[mid] < nums[mid + 1]`, move right because a peak exists on the right side.
- Otherwise, move left, keeping `mid` as a possible peak.

Continue until `low == high`.