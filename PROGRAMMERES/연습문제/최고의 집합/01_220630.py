def solution(n, s):
    answer = []
    if s == 1 or s < n:
        answer = [-1]
    elif s % n == 0:
        answer = [s // n] * n
    else:
        N = s // n
        answer = [N] * (n - s % n)
        answer += [N + 1] * (s % n)

    return answer