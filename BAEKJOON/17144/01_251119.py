# https://www.acmicpc.net/problem/17144
# 00:52:56

from collections import deque

drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def is_cir(r, c, air_r):
    return (r == air_r or r == air_r + 1) and c == 0


def spread(graph, R, C, air_r):
    q = deque([])
    for r in range(R):
        for c in range(C):
            if graph[r][c] > 0:
                q.append((r, c, graph[r][c]))

    while q:
        r, c, v = q.popleft()
        d = v // 5
        cnt = 0
        for dr, dc in drc:
            nr, nc = dr + r, dc + c
            if 0 <= nr < R and 0 <= nc < C and not is_cir(nr, nc, air_r):
                graph[nr][nc] += d
                cnt += 1
        graph[r][c] -= cnt * d

    for r in range(R):
        for c in range(C):
            if not is_cir(r, c, air_r) and graph[r][c] < 0:
                graph[r][c] = 0

    return graph


def circulate(air_r, graph, R, C):
    prev_u, curr_u = 0, 0
    prev_d, curr_d = 0, 0
    for c in range(1, C):
        curr_u = graph[air_r][c]
        graph[air_r][c] = prev_u
        prev_u = curr_u
        curr_d = graph[air_r + 1][c]
        graph[air_r + 1][c] = prev_d
        prev_d = curr_d

    for r in range(air_r - 1, -1, -1):
        curr_u = graph[r][C - 1]
        graph[r][C - 1] = prev_u
        prev_u = curr_u

    for r in range(air_r + 2, R):
        curr_d = graph[r][C - 1]
        graph[r][C - 1] = prev_d
        prev_d = curr_d

    for c in range(C - 2, -1, -1):
        curr_u = graph[0][c]
        graph[0][c] = prev_u
        prev_u = curr_u
        curr_d = graph[R - 1][c]
        graph[R - 1][c] = prev_d
        prev_d = curr_d

    for r in range(1, air_r):
        curr_u = graph[r][0]
        graph[r][0] = prev_u
        prev_u = curr_u

    for r in range(R - 2, air_r + 1, -1):
        curr_d = graph[r][0]
        graph[r][0] = prev_d
        prev_d = curr_d

    return graph


R, C, T = map(int, input().split())
sr = -1
graph = []

for r in range(R):
    row = list(map(int, input().split()))
    graph.append(row)
    if sr == -1:
        for c in range(C):
            if row[c] == -1:
                sr = r

for t in range(T):
    graph = circulate(sr, spread(graph, R, C, sr), R, C)

ans = sum([sum(row) for row in graph]) + 2
print(ans)
