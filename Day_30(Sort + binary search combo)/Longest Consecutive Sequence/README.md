# Longest Consecutive Sequence

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

Given an unsorted array of integers `nums`, return the length of the longest sequence of consecutive integers.

The consecutive numbers must appear in sequence numerically, but they do not need to be next to each other in the original array.

Your solution must run in `O(n log n)` time or better.

**Restriction:** Do not use `.sort()`, `sorted()`, or `bisect`. Implement your own Merge Sort or Quick Sort to arrange the array before finding the longest consecutive sequence. Alternatively, use a suitable approach that satisfies the required time complexity.

### Example 1:
**Input:** `nums = [100,4,200,1,3,2]`

**Output:** `4`

**Explanation:** The longest consecutive sequence is `[1,2,3,4]`, which has a length of `4`.

### Example 2:
**Input:** `nums = [0,3,7,2,5,8,4,6,0,1]`

**Output:** `9`

**Explanation:** The longest consecutive sequence is `[0,1,2,3,4,5,6,7,8]`, which has a length of `9`. Duplicate values do not increase the sequence length.

### Example 3:
**Input:** `nums = [1,0,1,2]`

**Output:** `3`

**Explanation:** The longest consecutive sequence is `[0,1,2]`, which has a length of `3`.

### Example 4:
**Input:** `nums = []`

**Output:** `0`

**Explanation:** An empty array contains no consecutive sequence.

### Constraints:
- `0 <= len(nums) <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

### Expected Complexity:
- **Time:** `O(n log n)` using a custom comparison-based sorting algorithm, followed by a linear scan.
- **Auxiliary Space:** `O(n)` for Merge Sort, excluding the output array.

**Follow-up:** Can you solve this problem in `O(n)` expected time using a hash set without sorting? How would you avoid counting the same consecutive sequence multiple times?