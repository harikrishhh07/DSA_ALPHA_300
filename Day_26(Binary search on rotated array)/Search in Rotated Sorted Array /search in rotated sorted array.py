class Solution:
    def search(self, nums, target):
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid

            # Check whether the left half is sorted
            if nums[lo] <= nums[mid]:

                # Is the target inside the sorted left half?
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            # Otherwise, the right half is sorted
            else:

                # Is the target inside the sorted right half?
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1