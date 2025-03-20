# https://school.programmers.co.kr/learn/courses/30/lessons/120871?language=python3
# 00:13:27

def calc_three(num):
    if num % 3 == 0 or "3" in str(num):
        return calc_three(num + 1)
    return num


def solution(n):
    answer = 0
    for i in range(n):
        answer = calc_three(answer + 1)
    return answer