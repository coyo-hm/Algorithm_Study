# https://www.acmicpc.net/problem/13549
# 00:10:45

import sys
from collections import deque

input = sys.stdin.readline

MAX_X = 100001
n, k = map(int, input().split())
distance = [int(1e9)] * MAX_X
distance[n] = 0
q = deque([n])

while q:
    x = q.popleft()
    curr = distance[x]
    if x == k:
        break
    if x > 0 and distance[x - 1] > curr + 1:
        distance[x - 1] = distance[x] + 1
        q.append(x - 1)
    if x + 1 < MAX_X and distance[x + 1] > curr + 1:
        distance[x + 1] = distance[x] + 1
        q.append(x + 1)
    if x * 2 < MAX_X and distance[x * 2] > curr:
        distance[x * 2] = distance[x]
        q.append(x * 2)

print(distance[k])