# Sqrt(x)

<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />

<hr>

Given a non-negative integer `x`, return the **integer square root** of `x`.

The integer square root is the greatest integer `k` such that `k * k <= x`.

Since the return type is an integer, the decimal portion of the square root must be discarded.

Implement the solution using **Binary Search on Answer**.

**Restriction:** Do not use `math.sqrt()`, `math.isqrt()`, `bisect`, or the exponentiation operator for computing the square root. Implement Binary Search manually using `low`, `high`, and `mid`.

### Example 1:

**Input:** `x = 4`

**Output:** `2`

**Explanation:** The square root of `4` is exactly `2`.

### Example 2:

**Input:** `x = 8`

**Output:** `2`

**Explanation:** The square root of `8` is approximately `2.828`. After discarding the decimal portion, the result is `2`.

### Example 3:

**Input:** `x = 15`

**Output:** `3`

**Explanation:** `3 * 3 = 9 <= 15`, while `4 * 4 = 16 > 15`. Therefore, the integer square root is `3`.

### Example 4:

**Input:** `x = 0`

**Output:** `0`

**Explanation:** The square root of zero is zero.

### Constraints:

- `0 <= x <= 2^31 - 1`

### Expected Complexity:

- Time: `O(log x)` for `x >= 2`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you calculate the integer square root without using any built-in mathematical functions?

**Important Hint:** If `mid * mid <= x`, store `mid` as a possible answer and search the right half. Otherwise, search the left half.