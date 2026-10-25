# Peak Index in a Mountain Array

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

Given a **mountain array** `arr`, return the index of its peak element.

An array is considered a mountain array if:

1. Its length is at least `3`.
2. There exists an index `i` such that `0 < i < arr.length - 1`.
3. Elements strictly increase from index `0` to index `i`.
4. Elements strictly decrease from index `i` to the last index.

The peak is the maximum element where the increasing sequence changes into a decreasing sequence.

Implement the solution using **Binary Search**.

**Restriction:** Do not use `bisect`, `max()`, `index()`, or built-in searching functions. Determine the peak by comparing adjacent elements and identifying the direction of the slope.

### Example 1:

**Input:** `arr = [0, 1, 0]`

**Output:** `1`

**Explanation:** The array increases from `0` to `1` and decreases from `1` to `0`. Therefore, the peak is at index `1`.

### Example 2:

**Input:** `arr = [0, 2, 1, 0]`

**Output:** `1`

**Explanation:** The element `2` is the highest point in the mountain array.

### Example 3:

**Input:** `arr = [1, 3, 5, 7, 6, 4, 2]`

**Output:** `3`

**Explanation:** The array strictly increases until the element `7` at index `3`, then strictly decreases.

### Example 4:

**Input:** `arr = [2, 5, 9, 12, 8, 3]`

**Output:** `3`

**Explanation:** The element `12` is the peak because the slope changes from increasing to decreasing at index `3`.

### Constraints:

- `3 <= arr.length <= 10^5`
- `0 <= arr[i] <= 10^6`
- `arr` is guaranteed to be a valid mountain array.

### Expected Complexity:

- Time: `O(log n)`
- Auxiliary Space: `O(1)`

**Follow-up:** Can you find the peak index without checking every element or using `max()`?

**Important Hint:** If `arr[mid] < arr[mid + 1]`, you are on the increasing slope, so search the right half. Otherwise, you are on the decreasing slope or at the peak, so search the left half including `mid`.