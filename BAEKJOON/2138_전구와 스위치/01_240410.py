# https://www.acmicpc.net/problem/2138
# 01:03:15

import sys

input = sys.stdin.readline

n = int(input())
curr = list(map(int, list(input().rstrip())))
target = list(map(int, list(input().rstrip())))


def switch(curr, target):
    temp = curr[:]
    cnt = 0
    for i in range(1, n):
        if temp[i - 1] == target[i - 1]:
            continue
        cnt += 1
        for j in range(i - 1, i + 2):
            if 0 <= j < n:
                temp[j] = 1 - temp[j]
    if temp == target:
        return cnt
    return 1e9


answer = switch(curr, target)
curr[0] = 1 - curr[0]
curr[1] = 1 - curr[1]
answer = min(answer, switch(curr, target) + 1)

if answer < 1e9:
    print(answer)
else:
    print(-1)
