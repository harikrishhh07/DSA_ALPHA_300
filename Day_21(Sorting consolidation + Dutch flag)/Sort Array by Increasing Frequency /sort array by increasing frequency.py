def frequency_sort(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and (
            freq[nums[j]] > freq[key]
            or (
                freq[nums[j]] == freq[key]
                and nums[j] < key
            )
        ):
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums


print(frequency_sort([1, 1, 2, 2, 2, 3]))
