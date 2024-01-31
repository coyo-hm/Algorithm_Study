# https://www.acmicpc.net/problem/17484
# 00:34:43

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dc = [-1, 0, 1]
answer = float("inf")


def dfs(r, c, curr, direction):
    global answer
    if r == N:
        answer = min(answer, curr)
        return
    for d in range(3):
        if d == direction:
            continue
        nr, nc = r + 1, c + dc[d]
        if nc >= M or nc < 0:
            continue
        dfs(nr, nc, curr + graph[r][c], d)


for sc in range(M):
    dfs(0, sc, 0, -1)

print(answer)
