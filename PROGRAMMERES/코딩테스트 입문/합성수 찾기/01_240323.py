# https://school.programmers.co.kr/learn/courses/30/lessons/120846
# 00:03:45

import math


def check(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return True
    return False


def solution(n):
    answer = 0
    for i in range(4, n + 1):
        if check(i):
            answer += 1
    return answer