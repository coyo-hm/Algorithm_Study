# https://www.acmicpc.net/problem/17484
# 1:10:19

import sys

input = sys.stdin.readline
dc = [-1, 0, 1]
INF = int(1e9)
fuel = INF
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def dfs(r, c, distance, direction):
    global fuel
    if r == N:
        fuel = min(fuel, distance)
        return

    for d in range(3):
        if d == direction:
            continue
        nr, nc = r + 1, c + dc[d]
        if nc >= M or nc < 0:
            continue
        dfs(nr, nc, distance + graph[r][c], d)


for sc in range(M):
    dfs(0, sc, 0, -1)

print(fuel)
