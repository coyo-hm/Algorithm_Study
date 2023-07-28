def solution(n, k, enemy):
    s, e = 0, len(enemy)
    while s <= e:
        m = (s + e) // 2
        temp = enemy[:m]
        temp.sort(reverse=True)
        st = sum(temp[k:])
        if st > n:
            e = m - 1
        else:
            s = m + 1

    return s - 1