import math
def solution(k, d):
    answer = 0
    p = (d ** 2) // (k ** 2)
    x = 0
    while x ** 2 <= p:
        y2 = p - x ** 2
        cnt = math.floor(y2 ** 0.5)
        if cnt >= 0:
            answer += cnt + 1
        x = x + 1
    return answer