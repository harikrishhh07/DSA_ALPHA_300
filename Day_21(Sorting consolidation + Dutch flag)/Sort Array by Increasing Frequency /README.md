# Sort Array by Increasing Frequency

<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />

<hr>

Given an array of integers `nums`, sort the elements by **increasing frequency**.

The frequency of an element is the number of times it appears in the array.

Follow these rules:

1. Elements with lower frequencies must appear before elements with higher frequencies.
2. If two elements have the same frequency, the larger element must appear first.

**Restriction:** Do not use `sort()`, `sorted()`, or `collections.Counter`. Build the frequency information manually and implement the sorting logic using loops, comparisons, and swaps. You may reuse your own sorting functions from previous days.

### Example 1:

**Input:** `nums = [1, 1, 2, 2, 2, 3]`

**Output:** `[3, 1, 1, 2, 2, 2]`

**Explanation:** The number `3` appears once, `1` appears twice, and `2` appears three times. Therefore, `3` comes first, followed by `1` and then `2`.

### Example 2:

**Input:** `nums = [2, 3, 1, 3, 2]`

**Output:** `[1, 3, 3, 2, 2]`

**Explanation:** The number `1` appears once. The numbers `2` and `3` each appear twice. Since equal frequencies are ordered by decreasing numerical value, `3` appears before `2`.

### Example 3:

**Input:** `nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]`

**Output:** `[5, -1, 4, 4, -6, -6, 1, 1, 1]`

**Explanation:** The numbers `5` and `-1` each appear once, so the larger number comes first. The numbers `4` and `-6` each appear twice, so `4` comes first. Finally, `1` appears three times.

### Constraints:

- `1 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`

### Expected Complexity:

Let `n` be the array length and `u` be the number of distinct values.

- Frequency counting: `O(n²)` using a simple manual search, or `O(n + r)` using a frequency array when the value range is bounded.
- Sorting: `O(u²)` using a manual comparison-based sorting algorithm.
- Auxiliary Space: `O(u)` for storing distinct values and their frequencies, excluding the output array.

**Follow-up:** Can you count each element's frequency once and then sort by frequency ascending, breaking ties by value descending, without using any built-in sorting function?

**Important Note:** The ordering must use both frequency and value. Sorting only by frequency will not correctly handle elements that occur the same number of times.