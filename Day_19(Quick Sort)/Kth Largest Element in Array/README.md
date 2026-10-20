# Kth Largest Element in Array (Partition Only)

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given an integer array `nums` and an integer `k`, return the **kth largest element** in the array.

The kth largest element is determined by sorting the array in descending order conceptually. It is not necessarily the kth distinct element.

Solve the problem using the **Quickselect algorithm**, which applies partitioning to locate the required element without fully sorting the array.

You may use Lomuto or Hoare partitioning, but ensure that your implementation correctly handles the chosen partition scheme.

**Restriction:** Do not use `sort()`, `sorted()`, or a complete sorting algorithm. Use partitioning to narrow the search to the region containing the kth largest element.

### Example 1:

**Input:** `nums = [3, 2, 1, 5, 6, 4]`, `k = 2`

**Output:** `5`

**Explanation:** The elements in descending order would be `[6, 5, 4, 3, 2, 1]`. The second largest element is `5`.

### Example 2:

**Input:** `nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]`, `k = 4`

**Output:** `4`

**Explanation:** The elements in descending order would be `[6, 5, 5, 4, 3, 3, 2, 2, 1]`. The fourth largest element is `4`.

### Example 3:

**Input:** `nums = [7, 7, 7, 7]`, `k = 2`

**Output:** `7`

**Explanation:** All elements have the same value, so the second largest element is `7`.

### Constraints:

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

### Expected Complexity:

- Average-case Time: `O(n)`
- Worst-case Time: `O(n^2)`
- Auxiliary Space: `O(1)` for an iterative in-place Quickselect implementation.

**Follow-up:** Can you solve the problem without sorting the entire array? Try selecting the kth largest element by targeting index `n - k` in ascending order.