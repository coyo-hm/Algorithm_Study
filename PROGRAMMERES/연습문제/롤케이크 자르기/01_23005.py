import collections


def solution(topping):
    answer = 0
    s1 = collections.Counter(topping)
    s2 = set([])

    for t in topping:
        s1[t] -= 1
        if s1[t] == 0:
            del s1[t]
        s2.add(t)
        if len(s1) == len(s2):
            answer += 1

    return answer