
def first_non_repeating(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for num in arr:
        if freq[num] == 1:
            return num
    return -1

print(first_non_repeating([4, 5, 1, 2, 0, 4]))
