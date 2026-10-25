# Valid Perfect Square

<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />

<hr>

Given a positive integer `num`, return `True` if `num` is a **perfect square**. Otherwise, return `False`.

A perfect square is an integer that can be expressed as the product of another integer with itself.

For example, `16` is a perfect square because `4 * 4 = 16`, while `14` is not.

Implement the solution using **Binary Search** to determine whether an integer exists whose square equals `num`.

**Restriction:** Do not use `math.sqrt()`, `math.isqrt()`, `bisect`, or built-in square-root operations. Implement the condition check and Binary Search manually.

### Example 1:

**Input:** `num = 16`

**Output:** `True`

**Explanation:** `4 * 4 = 16`, so `16` is a perfect square.

### Example 2:

**Input:** `num = 14`

**Output:** `False`

**Explanation:** No integer multiplied by itself produces `14`.

### Example 3:

**Input:** `num = 1`

**Output:** `True`

**Explanation:** `1 * 1 = 1`, so `1` is a perfect square.

### Example 4:

**Input:** `num = 25`

**Output:** `True`

**Explanation:** `5 * 5 = 25`, so the result is `True`.

### Constraints:

- `1 <= num <= 2^31 - 1`

### Expected Complexity:

- Time: `O(log num)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you determine whether a number is a perfect square without calculating its square root directly?

**Important Hint:** Compare `mid * mid` with `num`. If they are equal, return `True`. Otherwise, eliminate the half that cannot contain the answer.