from itertools import combinations


def solution(numbers):
    answer = list(set([sum(i) for i in list(combinations(numbers, 2))]))
    return sorted(answer)
