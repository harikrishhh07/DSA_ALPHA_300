# Counting Sort

<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />

<hr>

Given an array of integers `nums`, sort the array in ascending order using the **Counting Sort algorithm**.

Counting Sort works by counting the occurrences of each distinct integer within the input's value range. It then reconstructs the sorted array using these frequencies.

Build the frequency array manually and use the counts to produce the sorted result.

**Restriction:** Do not use `sort()`, `sorted()`, or `collections.Counter`. Implement the counting logic using arrays and loops.

### Example 1:

**Input:** `nums = [4, 2, 2, 8, 3, 3, 1]`

**Output:** `[1, 2, 2, 3, 3, 4, 8]`

**Explanation:** Count each value's occurrences and reconstruct the array in ascending order.

### Example 2:

**Input:** `nums = [5, 1, 4, 1, 2, 5]`

**Output:** `[1, 1, 2, 4, 5, 5]`

**Explanation:** The frequency array records that `1` and `5` each occur twice, while `2` and `4` each occur once.

### Example 3:

**Input:** `nums = [3, 3, 3, 3]`

**Output:** `[3, 3, 3, 3]`

**Explanation:** The value `3` occurs four times, so it is written four times into the output.

### Constraints:

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

### Expected Complexity:

Let `n` be the array length and `r` be the range of integer values.

- Time: `O(n + r)`
- Auxiliary Space: `O(r)` when the output is reconstructed in place, excluding the input array.

**Follow-up:** How would you handle negative integers when building the frequency array? Consider using an offset based on the minimum value.