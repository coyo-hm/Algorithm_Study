# https://school.programmers.co.kr/learn/courses/30/lessons/135808
# 00:07:58

def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    for i in range(m - 1, len(score), m):
        answer += score[i] * m
    return answer