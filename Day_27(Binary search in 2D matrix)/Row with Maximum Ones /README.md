# Row with Maximum Ones

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given a binary matrix `mat` of size `m x n`, find the index of the row containing the **maximum number of ones**.

Each row is sorted in non-decreasing order, meaning all zeros appear before all ones.

If multiple rows contain the same maximum number of ones, return the index of the first such row.

If the matrix contains no ones, return `-1`.

Implement the solution using **Binary Search** to locate the first occurrence of `1` in each row.

**Restriction:** Do not use `numpy`, `count()`, or built-in searching functions. Implement Binary Search manually to find the first `1` in every row.

### Example 1:

**Input:**
```text
mat = [
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 0]
]
```

**Output:** `1`

**Explanation:**

- Row `0` contains `1` one.
- Row `1` contains `3` ones.
- Row `2` contains `2` ones.
- Row `3` contains `0` ones.

Row `1` contains the maximum number of ones.

### Example 2:

**Input:**
```text
mat = [
    [0, 0],
    [0, 1],
    [0, 1]
]
```

**Output:** `1`

**Explanation:** Rows `1` and `2` each contain one `1`. Since ties are resolved by choosing the first row, return index `1`.

### Example 3:

**Input:**
```text
mat = [
    [0, 0, 0],
    [0, 0, 0]
]
```

**Output:** `-1`

**Explanation:** No row contains a `1`, so return `-1`.

### Example 4:

**Input:**
```text
mat = [
    [1, 1, 1],
    [0, 1, 1],
    [0, 0, 1]
]
```

**Output:** `0`

**Explanation:** Row `0` contains three ones, which is the maximum number of ones in the matrix.

### Constraints:

- `1 <= m, n <= 10^3`
- `mat[i][j]` is either `0` or `1`.
- Every row is sorted in non-decreasing order.

### Expected Complexity:

- Time: `O(m log n)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you solve the problem in `O(m + n)` time using a staircase traversal from the top-right corner?

**Important Hint:** In each row, use Binary Search to find the first index containing `1`. The number of ones is `n - first_one_index`. If no `1` exists, the row contains zero ones. Update the answer only when a row has strictly more ones than the current best, preserving the first row in case of a tie.