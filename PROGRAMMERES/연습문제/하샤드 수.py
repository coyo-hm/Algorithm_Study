def solution(x):
    h = sum(list(map(int, list(str(x)))))
    return x % h == 0