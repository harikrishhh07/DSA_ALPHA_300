# Search Insert Position

<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />

<hr>

Given a sorted array of distinct integers `nums` and an integer `target`, return the index if `target` is found.

If `target` is not found, return the index where it should be inserted so that the array remains sorted.

You must implement a solution using **Binary Search** with `O(log n)` time complexity.

**Restriction:** Do not use `bisect`, `bisect_left()`, `bisect_right()`, `sort()`, or `sorted()`. Implement the search manually using `low`, `high`, and `mid` pointers. Calculate the midpoint using `low + (high - low) // 2`.

### Example 1:

**Input:** `nums = [1, 3, 5, 6]`, `target = 5`

**Output:** `2`

**Explanation:** The target `5` exists at index `2`, so return that index.

### Example 2:

**Input:** `nums = [1, 3, 5, 6]`, `target = 2`

**Output:** `1`

**Explanation:** The target `2` is not present. Inserting it at index `1` produces `[1, 2, 3, 5, 6]`.

### Example 3:

**Input:** `nums = [1, 3, 5, 6]`, `target = 7`

**Output:** `4`

**Explanation:** The target is greater than every element, so it should be inserted at the end of the array.

### Example 4:

**Input:** `nums = [1, 3, 5, 6]`, `target = 0`

**Output:** `0`

**Explanation:** The target is smaller than every element, so it belongs at index `0`.

### Constraints:

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains distinct integers sorted in ascending order.
- `-10^4 <= target <= 10^4`

### Expected Complexity:

- Best-case Time: `O(1)`
- Worst-case Time: `O(log n)`
- Auxiliary Space: `O(1)` for the iterative implementation.

**Follow-up:** Can you solve this problem without inserting the target into the array? Return only the correct index.

**Important Hint:** When the target is greater than every element, the answer is `len(nums)`. When the target is smaller than every element, the answer is `0`. Binary Search can find both cases naturally.