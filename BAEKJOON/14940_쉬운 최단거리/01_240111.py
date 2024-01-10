# https://www.acmicpc.net/problem/14940
# 00:13:00

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
distance = [[-1] * m for _ in range(n)]
sr, sc = -1, -1
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for r in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for c in range(m):
        if row[c] == 2:
            sr, sc = r, c
        elif row[c] == 0:
            distance[r][c] = 0

q = deque([(sr, sc)])
distance[sr][sc] = 0

while q:
    r, c = q.popleft()
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and distance[nr][nc] == -1 and graph[nr][nc] == 1:
            distance[nr][nc] = distance[r][c] + 1
            q.append((nr, nc))

for r in range(n):
    for c in range(m):
        print(distance[r][c], end=" ")
    print()
