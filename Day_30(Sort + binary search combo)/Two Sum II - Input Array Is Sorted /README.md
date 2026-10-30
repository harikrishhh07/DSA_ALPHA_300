# Two Sum II — Input Array Is Sorted

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

Given a **1-indexed array** of integers `numbers` that is sorted in non-decreasing order, find two numbers whose sum equals the given integer `target`.

Return the indices of the two numbers as `[index1, index2]`, where:

- `1 <= index1 < index2 <= len(numbers)`.
- Each input has exactly one solution.
- You may not use the same element twice.

Your solution must use constant auxiliary space.

**Restriction:** Do not use `.sort()`, `sorted()`, or `bisect`. Since the input is already sorted, use two pointers or implement your own binary search to find the required pair.

### Example 1:
**Input:** `numbers = [2,7,11,15], target = 9`

**Output:** `[1,2]`

**Explanation:** `numbers[1] + numbers[2] = 2 + 7 = 9`. The returned indices are 1-based.

### Example 2:
**Input:** `numbers = [2,3,4], target = 6`

**Output:** `[1,3]`

**Explanation:** `numbers[1] + numbers[3] = 2 + 4 = 6`.

### Example 3:
**Input:** `numbers = [-1,0], target = -1`

**Output:** `[1,2]`

**Explanation:** `-1 + 0 = -1`, so the required indices are `[1,2]`.

### Constraints:
- `2 <= len(numbers) <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order.
- `-1000 <= target <= 1000`
- Exactly one valid solution exists.

### Expected Complexity:
- **Time:** `O(n)` using two pointers, or `O(n log n)` using binary search for each element.
- **Auxiliary Space:** `O(1)`.

**Follow-up:** Explain why the two-pointer approach is more efficient than checking every pair. If the current sum is smaller than the target, why is it safe to move the left pointer forward?