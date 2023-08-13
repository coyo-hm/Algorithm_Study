def score(i, n, s, info, scores):
    print(i, n, s, info, scores)
    if n == 0 or i == 0:
        a, b = 0, 0
        for i in range(11):
            if info[i] < scores[i]:
                b += 10 - i
            else:
                a += 10 - i
        if a > b:
            return [scores, -1]
        else:
            return [scores, b - a]

    if info[11 - i] >= n:
        return score(i - 1, n, s, info, scores)
    else:
        a = score(i - 1, n, s, info, scores)
        scores[11 - i] = info[11 - i] + 1
        b = score(i - 1, n - info[11 - i] - 1, s + i, info, scores)
        return a if a[1] >= b[1] else b


def solution(n, info):
    if info[0] == n:
        return [-1]
    answer = [0] * 11
    ans = score(11, n, 0, info, answer)
    print(ans)

    return answer