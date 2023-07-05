def hanoi(n, des, start, sup):
    if n == 1:
        return [[start, des]]
    return hanoi(n - 1, sup, start, des) + [[start, des]] + hanoi(n - 1, des, sup, start)


def solution(n):
    return hanoi(n, 3, 1, 2)