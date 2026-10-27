def row_with_max_ones(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    max_ones = 0
    answer = -1

    for r in range(rows):
        lo = 0
        hi = cols - 1
        first_one = cols

        # Find the first 1 in this row
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if matrix[r][mid] == 1:
                first_one = mid
                hi = mid - 1
            else:
                lo = mid + 1

        count = cols - first_one

        if count > max_ones:
            max_ones = count
            answer = r

    return answer


matrix = [
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

print(row_with_max_ones(matrix))