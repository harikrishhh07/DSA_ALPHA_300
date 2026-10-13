
def count_frequencies(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

arr = [1, 2, 2, 3, 1, 1]
freq = count_frequencies(arr)

for num in freq:
    print(num, "->", freq[num])
