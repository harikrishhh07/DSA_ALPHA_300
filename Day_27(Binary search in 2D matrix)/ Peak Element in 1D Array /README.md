# Peak Element in 1D Array

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given an integer array `nums`, find a **peak element** and return its index.

A peak element is an element that is strictly greater than its neighboring elements.

For the first and last elements, assume the elements outside the array have a value of negative infinity.

If multiple peaks exist, return the index of any one of them.

Your solution must run in `O(log n)` time using **Binary Search**.

**Restriction:** Do not use `bisect`, `max()`, `index()`, or any built-in searching function. Implement Binary Search manually by comparing adjacent elements and identifying the direction of the slope.

### Example 1:

**Input:** `nums = [1, 2, 3, 1]`

**Output:** `2`

**Explanation:** The element `3` at index `2` is greater than both neighboring elements, `2` and `1`. Therefore, index `2` is a peak.

### Example 2:

**Input:** `nums = [1, 2, 1, 3, 5, 6, 4]`

**Output:** `5`

**Explanation:** The element `6` at index `5` is greater than its neighbors, `5` and `4`. Another valid answer is index `1`, where the element `2` is also a peak.

### Example 3:

**Input:** `nums = [1]`

**Output:** `0`

**Explanation:** A single element is considered a peak because its imaginary neighbors are negative infinity.

### Example 4:

**Input:** `nums = [5, 4, 3, 2, 1]`

**Output:** `0`

**Explanation:** The first element `5` is greater than its right neighbor. Therefore, index `0` is a peak.

### Constraints:

- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid adjacent indices.

### Expected Complexity:

- Best-case Time: `O(1)`
- Worst-case Time: `O(log n)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you find a peak element without scanning the entire array?

**Important Hint:** Compare `nums[mid]` with `nums[mid + 1]`.

- If `nums[mid] < nums[mid + 1]`, the slope is rising. Search the right half.
- Otherwise, the slope is falling or the middle element is a peak. Search the left half, including `mid`.

Continue until `low == high`. The remaining index identifies a peak.