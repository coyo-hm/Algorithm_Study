# https://www.acmicpc.net/problem/21610

import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move_arr = [list(map(int, input().split())) for _ in range(m)]
cloud = collections.deque([(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)])
prev_cloud = []

dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

dxr = [1, 1, -1, -1]
dxc = [1, -1, 1, -1]

for d, s in move_arr:
    while cloud:
        r, c = cloud.popleft()
        nr = (r + n + dr[d] * s) % n
        nc = (c + n + dc[d] * s) % n
        prev_cloud.append((nr, nc))
        graph[nr][nc] += 1

    for r, c in prev_cloud:
        cnt = 0
        for dx in range(4):
            nr = r + dxr[dx]
            nc = c + dxc[dx]
            if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] > 0:
                cnt += 1
        graph[r][c] += cnt

    visited = [[0] * n for _ in range(n)]

    for r, c in prev_cloud:
        visited[r][c] = 1

    for r in range(n):
        for c in range(n):
            if graph[r][c] >= 2 and visited[r][c] == 0:
                cloud.append((r, c))
                graph[r][c] = graph[r][c] - 2 if graph[r][c] - 2 >= 0 else 0

    prev_cloud = []

ans = 0

for r in range(n):
    for c in range(n):
        ans += graph[r][c]

print(ans)