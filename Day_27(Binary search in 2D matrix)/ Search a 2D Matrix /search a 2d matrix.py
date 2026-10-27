class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        lo = 0
        hi = rows * cols - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False