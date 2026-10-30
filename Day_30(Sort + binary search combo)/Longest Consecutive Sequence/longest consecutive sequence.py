class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums = merge_sort(nums)

        longest = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            elif nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                current = 1

            if current > longest:
                longest = current

        return longest