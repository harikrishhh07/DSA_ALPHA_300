def guess(num):
    if num == pick:
        return 0
    elif num < pick:
        return 1
    else:
        return -1

class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == 1:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1

n = 10
pick = 6
obj = Solution()
print(obj.guessNumber(n))
