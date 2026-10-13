def totalFruit(fruits):
    left = 0
    count = {}
    ans = 0
    for right in range(len(fruits)):
        x = fruits[right]
        count[x] = count.get(x, 0) + 1
        while len(count) > 2:
            y = fruits[left]
            count[y] -= 1
            if count[y] == 0:
                del count[y]
            left += 1
        ans = max(ans, right - left + 1)

    return ans