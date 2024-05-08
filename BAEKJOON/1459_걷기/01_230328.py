# https://www.acmicpc.net/problem/1459

import sys

input = sys.stdin.readline

n, m, w, s = map(int, input().split())
ans = 0

if 2 * w > s:
    c = min(n, m)
    ans += c * s
    n -= c
    m -= c

if w > s:
    dn = n % 2
    dm = m % 2
    ans += (n + m - dn - dm) * s
    n = dn
    m = dm

ans += (n + m) * w

print(ans)
