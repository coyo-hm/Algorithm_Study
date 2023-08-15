from itertools import product

def solution(n, info):
    info.reverse()
    m = 0
    answer = [-1]
    for case in product([True, False], repeat = 11):
        cnt = sum([info[i] + 1 for i in range(11) if case[i] == True])
        if cnt <= n:
            apeach = sum(i for i in range(11) if case[i] == False and info[i] != 0)
            ryan = sum(i for i in range(11) if case[i] == True)
            s = ryan - apeach
            if s > m:
                m = s
                answer = [info[i] + 1 if case[i] == True else 0 for i in range(11)]
                answer[0] = n - cnt
    answer.reverse()
    return answer