def check(q, r, c):
    for i in range(r):
        if q[i] == c or abs(q[i] - c) == (r - i):
            return False
    return True


def dfs(q, n, r):
    if n == r:
        return 1
    cnt = 0
    for c in range(n):
        if check(q, r, c):
            q[r] = c
            cnt += dfs(q, n, r + 1)
    return cnt


def solution(n):
    q = [0] * n
    return dfs(q, n, 0)