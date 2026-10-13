def longestSubarraySumK(nums, k):
    left = 0
    curr_sum = 0
    longest = 0
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1
        if curr_sum == k:
            longest = max(longest, right - left + 1)

    return longest
