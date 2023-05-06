def solution(a, b):
    return sum(list(map(lambda x: a[x]*b[x], [i for i in range(len(a))])))