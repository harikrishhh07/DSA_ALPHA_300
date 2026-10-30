# 3Sum

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that:

- `i`, `j`, and `k` are distinct indices.
- `nums[i] + nums[j] + nums[k] == 0`.
- The resulting list must not contain duplicate triplets.

Return the triplets in any order.

**Restriction:** Do not use `.sort()`, `sorted()`, or `bisect`. Implement your own Merge Sort or Quick Sort to arrange the array in ascending order. Then use a fixed first element and two pointers to find triplets whose sum is zero. Skip duplicate values to avoid repeated triplets.

### Example 1:
**Input:** `nums = [-1,0,1,2,-1,-4]`

**Output:** `[[-1,-1,2],[-1,0,1]]`

**Explanation:**
- Sort the array: `[-4,-1,-1,0,1,2]`.
- Fix the first `-1`. The pair `[-1,2]` produces the triplet `[-1,-1,2]`.
- The pair `[0,1]` produces the triplet `[-1,0,1]`.
- Duplicate triplets are skipped.

### Example 2:
**Input:** `nums = [0,1,1]`

**Output:** `[]`

**Explanation:** No three numbers sum to zero.

### Example 3:
**Input:** `nums = [0,0,0]`

**Output:** `[[0,0,0]]`

**Explanation:** The three zeros form one valid triplet. Duplicate combinations must not be returned.

### Constraints:
- `3 <= len(nums) <= 3000`
- `-10^5 <= nums[i] <= 10^5`

### Expected Complexity:
- **Time:** `O(n^2)` for the two-pointer search, after `O(n log n)` sorting.
- **Auxiliary Space:** `O(n)` for Merge Sort, excluding the output array. The two-pointer search itself uses `O(1)` additional space.

**Follow-up:** Why does sorting allow you to move the left pointer forward when the sum is too small and the right pointer backward when the sum is too large? Explain how skipping duplicate values prevents repeated triplets.