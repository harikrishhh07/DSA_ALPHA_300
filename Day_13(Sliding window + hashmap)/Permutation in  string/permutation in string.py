def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    a, b = {}, {}
    for c in s1:
        a[c] = a.get(c, 0) + 1
    for c in s2[:len(s1)]:
        b[c] = b.get(c, 0) + 1
    if a == b:
        return True
    for i in range(len(s1), len(s2)):
        x = s2[i]
        y = s2[i - len(s1)]
        b[x] = b.get(x, 0) + 1
        b[y] -= 1
        if b[y] == 0:
            del b[y]
        if a == b:
            return True
    return False