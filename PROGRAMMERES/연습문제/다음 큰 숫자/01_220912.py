def solution(n):
    b = bin(n)[2:]
    r = n + 1

    while b.count("1") != bin(r)[2:].count("1"):
        r += 1
    return r