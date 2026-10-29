# Allocate Minimum Pages (GFG)

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

You are given an array `arr`, where `arr[i]` represents the number of pages in the `i-th` book, and an integer `k`, representing the number of students.

Allocate all books among the students according to these rules:

- Each student must receive at least one book.
- Each book must be allocated to exactly one student.
- Books must be allocated in their original order, so each student receives a **contiguous sequence of books**.
- The objective is to **minimize the maximum number of pages assigned to any student**.

Return the minimum possible maximum number of pages. If the number of students exceeds the number of books, return `-1`.

**Restriction:** Do not use `bisect`. Use binary search on the answer and implement a feasibility check that determines whether the books can be allocated to at most `k` students without any student exceeding the tested page limit.

### Example 1:
**Input:** `arr = [12,34,67,90], k = 2`

**Output:** `113`

**Explanation:** One optimal allocation is:

- Student 1: `[12,34,67]` — total `113` pages
- Student 2: `[90]` — total `90` pages

The maximum is `113` pages, and no valid allocation can achieve a smaller maximum.

### Example 2:
**Input:** `arr = [15,17,20], k = 2`

**Output:** `32`

**Explanation:** One optimal allocation is `[15,17]` and `[20]`. The maximum pages assigned to a student is `32`.

### Example 3:
**Input:** `arr = [10,20], k = 3`

**Output:** `-1`

**Explanation:** There are only two books, so it is impossible to give at least one book to each of the three students.

### Constraints:
- `1 <= len(arr) <= 10^5`
- `1 <= arr[i] <= 10^3`
- `1 <= k <= 10^5`

### Expected Complexity:
- **Time:** `O(n log S)`, where `S` is the sum of all pages.
- **Auxiliary Space:** `O(1)`

**Follow-up:** How is this problem similar to Capacity to Ship Packages Within D Days? Identify the lower bound, upper bound, and feasibility condition for the binary search.