import math

def solution(n, stations, w):
    answer = 0
    idx = -1 * w
    b = 2 * w + 1

    for s in stations:
        answer += math.ceil((s - idx - b) / b)
        idx = s
    answer += math.ceil((n - idx - w) / b)

    return answer