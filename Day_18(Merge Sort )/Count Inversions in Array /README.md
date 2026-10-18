# Count Inversions in Array

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given an array of integers `nums`, count the number of **inversions** in the array.

An inversion is a pair of indices `(i, j)` such that:

- `i < j`
- `nums[i] > nums[j]`

In other words, an inversion occurs when a larger element appears before a smaller element.

Your goal is to return the total number of inversions in the array.

**Restriction:** Do not use `sort()`, `sorted()`, or any built-in sorting function. For an efficient solution, modify the Merge Sort algorithm to count inversions during the merging process.

### Example 1:

**Input:** `nums = [2, 4, 1, 3, 5]`

**Output:** `3`

**Explanation:** The inversion pairs are `(2, 1)`, `(4, 1)`, and `(4, 3)`. Therefore, the total number of inversions is `3`.

### Example 2:

**Input:** `nums = [5, 4, 3, 2, 1]`

**Output:** `10`

**Explanation:** Every pair of elements that appears in reverse order forms an inversion. The total is `4 + 3 + 2 + 1 = 10`.

### Example 3:

**Input:** `nums = [1, 2, 3, 4, 5]`

**Output:** `0`

**Explanation:** The array is already sorted in ascending order. No pair satisfies the inversion condition.

### Example 4:

**Input:** `nums = [1, 1, 1]`

**Output:** `0`

**Explanation:** Equal elements do not form inversions because the condition requires `nums[i] > nums[j]`.

### Constraints:

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

### Expected Complexity:

- Time: `O(n log n)`
- Auxiliary Space: `O(n)`, excluding recursion-stack space.

### Important Hint:

During the merge step, if the current element in the left sorted half is greater than the current element in the right sorted half, then that right-side element forms an inversion with every remaining element in the left half.

If the left pointer is at index `i` and the midpoint is `mid`, the number of new inversions is:

`mid - i + 1`

**Follow-up:** Can you count inversions in `O(n log n)` time instead of comparing every possible pair in `O(n²)` time?