# https://www.acmicpc.net/problem/20055
# 00:28:20

import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
belts = deque(list(map(int, input().split())))
robots = deque([0] * n)
answer, zero_cnt = 0, 0

while zero_cnt < k:
    belts.rotate(1)
    robots.rotate(1)
    robots[-1] = 0
    for i in range(n - 2, -1, -1):
        if robots[i] == 1 and belts[i + 1] > 0 and robots[i + 1] == 0:
            belts[i + 1] -= 1
            robots[i] = 0
            robots[i + 1] = 1
    robots[-1] = 0
    if robots[0] == 0 and belts[0] > 0:
        belts[0] -= 1
        robots[0] = 1
    answer += 1
    zero_cnt = belts.count(0)

print(answer)
