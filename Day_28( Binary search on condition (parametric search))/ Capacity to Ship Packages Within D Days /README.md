# Capacity to Ship Packages Within D Days

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

You are given an array `weights`, where `weights[i]` represents the weight of the `i-th` package, and an integer `days`.

Packages must be shipped in the **same order as given**. Each day, you load a consecutive sequence of packages onto the ship without exceeding its capacity.

Return the **minimum ship capacity** required to ship all packages within `days` days.

**Restriction:** Do not use `bisect`. Use binary search on the answer and implement a feasibility check to determine whether a given capacity can ship all packages within the required number of days.

### Example 1:
**Input:** `weights = [1,2,3,4,5,6,7,8,9,10], days = 5`

**Output:** `15`

**Explanation:** With capacity `15`, the packages can be shipped in five days:

- Day 1: `[1,2,3,4,5]` — total `15`
- Day 2: `[6,7]` — total `13`
- Day 3: `[8]` — total `8`
- Day 4: `[9]` — total `9`
- Day 5: `[10]` — total `10`

A capacity smaller than `15` cannot ship all packages within five days.

### Example 2:
**Input:** `weights = [3,2,2,4,1,4], days = 3`

**Output:** `6`

**Explanation:** One valid arrangement is `[3,2]`, `[2,4]`, and `[1,4]`. Each day's total weight is at most `6`.

### Example 3:
**Input:** `weights = [1,2,3,1,1], days = 4`

**Output:** `3`

**Explanation:** A capacity of `3` is sufficient to ship the packages in four days.

### Constraints:
- `1 <= days <= len(weights) <= 5 * 10^4`
- `1 <= weights[i] <= 500`

### Expected Complexity:
- **Time:** `O(n log S)`, where `n` is the number of packages and `S` is the sum of all package weights.
- **Auxiliary Space:** `O(1)`

**Follow-up:** Explain why the answer must lie between the maximum package weight and the sum of all package weights. Why does feasibility change monotonically as capacity increases?