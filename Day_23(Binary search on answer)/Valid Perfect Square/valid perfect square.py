class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 1
        hi = num
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                lo = mid + 1
            else:
                hi = mid - 1

        return False
