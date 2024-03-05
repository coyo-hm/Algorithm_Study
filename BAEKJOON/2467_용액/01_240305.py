# https://www.acmicpc.net/problem/2467
# 00:21:15

import sys

input = sys.stdin.readline
n = int(input())
solution = list(map(int, input().split()))

l, r = 0, n - 1
gap = int(1e9) * 2
answer_l, answer_r = 0, 0

while l < r:
    m = solution[l] + solution[r]
    # print(m, solution[l] , solution[r])
    if abs(m) < gap:
        gap = abs(m)
        answer_l = solution[l]
        answer_r = solution[r]
    if m > 0:
        r -= 1
    else:
        l += 1


# print(gap)
print(answer_l, answer_r)
