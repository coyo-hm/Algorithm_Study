def solution(n):
    return int("".join([i for i in sorted(str(n), reverse = True)]))