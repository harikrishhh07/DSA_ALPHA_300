# First Bad Version

<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />

<hr>

You are given `n` versions numbered from `1` to `n`.

Suppose you are developing a product and want to identify the **first bad version** that causes all subsequent versions to be bad.

You are given a Boolean API `isBadVersion(version)` that returns:

- `True` if the version is bad.
- `False` if the version is good.

Once a version becomes bad, every version after it is also bad.

Implement the function `firstBadVersion(n)` to return the first bad version while minimizing the number of API calls.

**Restriction:** Do not use `bisect`, `bisect_left()`, or `bisect_right()`. Use Binary Search manually with `low`, `high`, and `mid` pointers. Calculate the midpoint using `low + (high - low) // 2`.

### Example 1:

**Input:** `n = 5`, `bad = 4`

**Output:** `4`

**Explanation:** Versions `1`, `2`, and `3` are good, while versions `4` and `5` are bad. Binary Search identifies version `4` as the first bad version.

### Example 2:

**Input:** `n = 1`, `bad = 1`

**Output:** `1`

**Explanation:** There is only one version, and it is bad. Therefore, the first bad version is `1`.

### Example 3:

**Input:** `n = 10`, `bad = 1`

**Output:** `1`

**Explanation:** The first version is already bad, so the answer is `1`.

### Constraints:

- `1 <= bad <= n <= 2^31 - 1`
- The API `isBadVersion(version)` is provided by the problem environment.
- Every version after the first bad version is also bad.

### Expected Complexity:

- Time: `O(log n)` API calls.
- Auxiliary Space: `O(1)` for the iterative implementation.

### Important Hint:

If `isBadVersion(mid)` returns `True`, the first bad version could be `mid` itself or an earlier version. Therefore, set `high = mid`.

If it returns `False`, the first bad version must be after `mid`. Therefore, set `low = mid + 1`.

Continue until `low == high`. That index is the first bad version.

**Follow-up:** Why should you set `high = mid` instead of `high = mid - 1` when the middle version is bad?