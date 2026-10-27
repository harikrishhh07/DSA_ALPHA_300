class Solution:
    def findMin(self, nums):
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] > nums[hi]:
                # Minimum must be to the right
                lo = mid + 1
            else:
                # Minimum is at mid or to the left
                hi = mid

        return nums[lo]