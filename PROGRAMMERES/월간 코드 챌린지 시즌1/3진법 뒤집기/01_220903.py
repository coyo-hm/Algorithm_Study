def solution(n):
    return int(makeThree(n, 3)[::-1], 3)


def makeThree(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]
