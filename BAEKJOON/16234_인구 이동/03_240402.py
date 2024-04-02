# https://www.acmicpc.net/problem/16234
# 00:23:47

import sys
from collections import deque

input = sys.stdin.readline
n, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

drc = [(1, 0), (-1, 0), (0, -1), (0, 1)]
visited = [[False] * n for _ in range(n)]
answer = 0


def move(sr, sc):
    global graph, visited
    countries = [(sr, sc)]
    pop_sum = graph[sr][sc]
    q = deque(countries)
    visited[sr][sc] = True

    while q:
        r, c = q.popleft()
        for dr, dc in drc:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < n and 0 <= nc < n and L <= abs(graph[r][c] - graph[nr][nc]) <= R and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))
                countries.append((nr, nc))
                pop_sum += graph[nr][nc]

    length = len(countries)
    if length <= 1:
        return

    p = pop_sum // length
    for r, c in countries:
        graph[r][c] = p


while True:
    cnt = 0
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                move(r, c)
                cnt += 1
    if cnt == n * n:
        break
    answer += 1
    visited = [[False] * n for _ in range(n)]

print(answer)
