from itertools import product


def solution(users, emoticons):
    rate = [10, 20, 30, 40]
    m = len(emoticons)
    price = [[e * (1 - r * 0.01) for r in rate] for e in emoticons]
    emo = list(product(range(4), repeat=m))
    cnt = 0
    pay = 0

    for idx in emo:
        c, p = 0, 0
        for u in users:
            m = sum([price[i][e] for (i, e) in enumerate(idx) if rate[e] >= u[0]])
            if m >= u[1]:
                c += 1
            else:
                p += m
        if c > cnt or (c == cnt and p >= pay):
            cnt = c
            pay = p
    return [cnt, pay]