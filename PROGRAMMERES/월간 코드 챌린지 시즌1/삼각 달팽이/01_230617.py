def solution(n):
    answer = [[] for _ in range(n)]
    num = 1
    for i in range(n):
        plus = list(range(num, num + n - i))
        if i % 3 == 0:
            s = (i // 3) * 2
            for l in range(n - i):
                answer[s + l].insert(i // 3, plus[l])
        elif i % 3 == 1:
            answer[n - 1 - i // 3] = answer[n - 1 - i // 3][:i // 3 + 1] + plus + answer[n - 1 - i // 3][i // 3 + 1:]
        elif i % 3 == 2:
            s = (i // 3) * 2 + n - i
            for l in range(n - i):
                # print(s - l, plus[l])
                idx = -1 * (i // 3) if len(answer[s - l]) > 1 else 2
                answer[s - l].insert(idx, plus[l])
        num += n - i

    # print(answer)
    res = []
    for r in answer:
        res = res + r
    return res