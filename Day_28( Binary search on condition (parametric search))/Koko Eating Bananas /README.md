# Koko Eating Bananas

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

Koko has `n` piles of bananas, where `piles[i]` represents the number of bananas in the `i-th` pile. She has `h` hours to finish eating all the bananas.

Koko chooses an integer eating speed `k` bananas per hour. During each hour, she chooses one pile and eats up to `k` bananas from that pile. If the pile contains fewer than `k` bananas, she finishes that pile but cannot use the remaining time in that hour to eat from another pile.

Return the **minimum integer eating speed** that allows Koko to finish all the bananas within `h` hours.

**Restriction:** Do not use `bisect`. Apply binary search on the possible eating speeds and write a feasibility check to calculate whether a speed can finish all piles within `h` hours.

### Example 1:
**Input:** `piles = [3,6,7,11], h = 8`

**Output:** `4`

**Explanation:** At a speed of `4` bananas per hour, the required hours are:

- Pile `3`: `1` hour
- Pile `6`: `2` hours
- Pile `7`: `2` hours
- Pile `11`: `3` hours

Total: `1 + 2 + 2 + 3 = 8` hours. A lower speed would require more than eight hours.

### Example 2:
**Input:** `piles = [30,11,23,4,20], h = 5`

**Output:** `30`

**Explanation:** Koko must finish five piles in five hours, so she needs to finish each pile in one hour. The minimum feasible speed is `30`.

### Example 3:
**Input:** `piles = [30,11,23,4,20], h = 6`

**Output:** `23`

**Explanation:** At speed `23`, the required hours are `2 + 1 + 1 + 1 + 1 = 6`.

### Constraints:
- `1 <= len(piles) <= 10^4`
- `1 <= piles[i] <= 10^9`
- `len(piles) <= h <= 10^9`

### Expected Complexity:
- **Time:** `O(n log M)`, where `M` is the maximum pile size.
- **Auxiliary Space:** `O(1)`

**Follow-up:** Why is the maximum pile size a sufficient upper bound for the answer? Explain why, if a speed is feasible, every higher speed is also feasible.