# https://www.acmicpc.net/problem/2512
# 0:06:03

import sys
input = sys.stdin.readline
N = int(input())
budgets = list(map(int, input().split()))
M = int(input())
s, e = 0, max(budgets)

while s <= e:
    m = (s + e) // 2
    total = 0
    for b in budgets:
        if b > m:
            total += m
        else:
            total += b

    if total > M:
        e = m - 1
    else:
        s = m + 1

print(e)