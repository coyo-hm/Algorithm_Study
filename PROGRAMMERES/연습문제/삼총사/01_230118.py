import itertools

def solution(number):
    arr = [sum(i) for i in itertools.combinations(number, 3)]
    return arr.count(0)