from collections import deque


def findMin(q, ans):
    if len(q) < 1:
        return ans
    n = int(q.pop())
    # print(q, n, ans)
    if n == 5:
        m = int("".join(q)) if len(q) > 0 else 0
        u = findMin(deque(str(m + 1)), ans + n)
        d = findMin(q, ans + n)
        return min(u, d)
    elif n > 5:
        m = int("".join(q)) if len(q) > 0 else 0
        return findMin(deque(str(m + 1)), ans + 10 - n)

    return findMin(q, ans + n)


def solution(storey):
    ans = findMin(deque(str(storey)), 0)
    return ans