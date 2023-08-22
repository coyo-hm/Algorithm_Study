def solution(n, l, r):
    answer = 0
    for i in range(l - 1, r):
        while i % 5 != 2 and i > 0:
            i = i // 5
        if i == 0:
            answer += 1
    return answer