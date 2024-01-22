# https://www.acmicpc.net/problem/13549
# 00:13:19

import sys
from collections import deque

input = sys.stdin.readline
MAX_NUM = 100001

n, k = map(int, input().split())
q = deque([n])
distance = [float("inf")] * MAX_NUM
distance[n] = 0

while q:
    curr = q.popleft()
    if curr + 1 < MAX_NUM and distance[curr + 1] > distance[curr] + 1:
        distance[curr + 1] = distance[curr] + 1
        q.append(curr + 1)
    if curr - 1 > -1 and distance[curr - 1] > distance[curr] + 1:
        distance[curr - 1] = distance[curr] + 1
        q.append(curr - 1)
    if curr * 2 < MAX_NUM and distance[curr] < distance[curr * 2]:
        distance[curr * 2] = distance[curr]
        q.append(curr * 2)

print(distance[k])
