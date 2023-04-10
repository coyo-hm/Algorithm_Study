def solution(stones, k):
    s, e = 1, max(stones)
    while s <= e:
        m = (s + e) // 2
        cnt = 0
        for st in stones:
            if st - m <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break

        if cnt >= k:
            e = m - 1
        else:
            s = m + 1
    return s