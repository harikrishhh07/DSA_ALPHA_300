# Search a 2D Matrix

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

You are given an `m x n` matrix of integers with the following properties:

1. Each row is sorted in ascending order.
2. The first element of each row is greater than the last element of the previous row.

Given an integer `target`, return `True` if the target exists in the matrix. Otherwise, return `False`.

Implement the solution using **Binary Search** by treating the matrix as a single sorted one-dimensional array without actually flattening it.

**Restriction:** Do not use `numpy`, `bisect`, `bisect_left()`, `bisect_right()`, or a separate flattened array. Use index arithmetic to access matrix elements.

For a matrix with `n` columns, convert a virtual one-dimensional index `mid` into matrix coordinates:

- Row index: `mid // n`
- Column index: `mid % n`

### Example 1:

**Input:**
```text
matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3
```

**Output:** `True`

**Explanation:** Binary Search treats the matrix as `[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]`. The target `3` is found at row `0`, column `1`.

### Example 2:

**Input:**
```text
matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 13
```

**Output:** `False`

**Explanation:** The target `13` does not exist in the matrix. Binary Search eliminates the remaining candidate positions and returns `False`.

### Example 3:

**Input:** `matrix = [[1]]`, `target = 1`

**Output:** `True`

**Explanation:** The matrix contains only one element, and it matches the target.

### Constraints:

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`
- Each row is sorted in ascending order.
- The first element of each row is greater than the last element of the previous row.

### Expected Complexity:

- Time: `O(log(m * n))`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you search the matrix without creating a separate one-dimensional array?

**Important Hint:** Initialize `low = 0` and `high = m * n - 1`. Convert every midpoint into row and column indices using integer division and modulo.