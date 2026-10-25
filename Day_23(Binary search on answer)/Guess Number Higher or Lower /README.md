# Guess Number Higher or Lower

<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />

<hr>

You are playing a guessing game. A secret number `pick` is chosen from the range `[1, n]`.

Your task is to identify the secret number using **Binary Search**.

You are provided with an API `guess(num)` that returns:

- `-1` if your guess is higher than the secret number.
- `1` if your guess is lower than the secret number.
- `0` if your guess is correct.

Implement the function `guessNumber(n)` to return the secret number while minimizing the number of API calls.

**Restriction:** Do not use `bisect`, `bisect_left()`, or `bisect_right()`. Implement Binary Search manually and calculate the midpoint using `low + (high - low) // 2`.

### Example 1:

**Input:** `n = 10`, `pick = 6`

**Output:** `6`

**Explanation:** Binary Search repeatedly narrows the possible range until it identifies the secret number `6`.

### Example 2:

**Input:** `n = 1`, `pick = 1`

**Output:** `1`

**Explanation:** Only one number is available, so the secret number must be `1`.

### Example 3:

**Input:** `n = 100`, `pick = 73`

**Output:** `73`

**Explanation:** The algorithm eliminates approximately half of the remaining candidates after each incorrect guess.

### Constraints:

- `1 <= n <= 2^31 - 1`
- `1 <= pick <= n`
- The `guess(num)` API is provided by the problem environment.

### Expected Complexity:

- Time: `O(log n)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you identify the secret number using logarithmically many API calls rather than checking every number?

**Important Hint:** If `guess(mid) == -1`, search the left half. If `guess(mid) == 1`, search the right half.