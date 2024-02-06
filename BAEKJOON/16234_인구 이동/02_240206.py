# https://www.acmicpc.net/problem/16234
# 0:43:27

import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]
answer = 0

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
visited = [[False] * N for _ in range(N)]


def union(sr, sc):
    global countries, answer, visited
    united = [(sr, sc)]
    countries_total = countries[sr][sc]

    q = deque([(sr, sc)])
    visited[sr][sc] = True

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 > nr or nr >= N or 0 > nc or nc >= N or visited[nr][nc]:
                continue
            diff = abs(countries[r][c] - countries[nr][nc])
            if diff > R or diff < L:
                continue
            visited[nr][nc] = True
            q.append((nr, nc))
            united.append((nr, nc))
            countries_total += countries[nr][nc]

    countries_cnt = len(united)
    if countries_cnt < 2:
        return

    new_population = countries_total // countries_cnt
    for r, c in united:
        countries[r][c] = new_population


while True:
    visited = [[False] * N for _ in range(N)]
    visited_cnt = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                union(r, c)
                visited_cnt += 1
    if visited_cnt == N * N:
        break
    answer += 1
print(answer)
