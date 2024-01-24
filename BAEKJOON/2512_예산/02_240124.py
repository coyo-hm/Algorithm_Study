# https://www.acmicpc.net/problem/2512
# 00:12:22

import sys

input = sys.stdin.readline
N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

s, e = 1, max(budgets)
while s <= e:
    m = (s + e) // 2

    total = 0
    for b in budgets:
        total += b if b < m else m

    if total <= M:
        s = m + 1
    else:
        e = m - 1

print(e)
