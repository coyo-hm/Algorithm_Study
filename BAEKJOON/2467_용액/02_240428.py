# https://www.acmicpc.net/problem/2467
# 00:10:15

import sys

input = sys.stdin.readline
n = int(input())
solutions = list(map(int, input().split()))

l, r = 0, n - 1
v = int(1e9) * 2
answer = (0, 0)

while l < r:
    new_v = solutions[l] + solutions[r]
    if abs(new_v) < v:
        v = abs(new_v)
        answer = (solutions[l], solutions[r])

    if new_v > 0:
        r -= 1
    else:
        l += 1

for a in answer:
    print(a, end=" ")