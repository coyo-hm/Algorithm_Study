# https://www.acmicpc.net/problem/14940
# 00:09:30

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
distance = [[-1] * m for _ in range(n)]
q = deque([])

for r in range(n):
    row = list(map(int, input().split()))
    for c in range(m):
        if row[c] == 2:
            q.append((r, c))
            distance[r][c] = 0
        elif row[c] == 0:
            distance[r][c] = 0
    graph.append(row)

while q:
    r, c = q.popleft()
    for d in range(4):
        nr = dr[d] + r
        nc = dc[d] + c
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 1 and distance[nr][nc] == -1:
            distance[nr][nc] = distance[r][c] + 1
            q.append((nr, nc))

for r in range(n):
    for c in range(m):
        print(distance[r][c], end=" ")
    print()
