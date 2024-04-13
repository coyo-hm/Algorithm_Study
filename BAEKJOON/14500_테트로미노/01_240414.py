# https://www.acmicpc.net/problem/14500
# 00:48:38

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

tetris = [[(0, 0), (0, 1), (0, 2), (0, 3)],
          [(0, 0), (1, 0), (2, 0), (3, 0)],
          [(0, 0), (1, 0), (0, 1), (1, 1)],
          [(0, 0), (1, 0), (2, 0), (2, 1)],
          [(0, 1), (1, 1), (2, 1), (2, 0)],
          [(0, 0), (0, 1), (1, 1), (2, 1)],
          [(0, 0), (0, 1), (1, 0), (2, 0)],
          [(0, 0), (1, 0), (1, 1), (1, 2)],
          [(0, 2), (1, 1), (1, 2), (1, 0)],
          [(0, 0), (0, 1), (0, 2), (1, 2)],
          [(0, 0), (1, 0), (0, 1), (0, 2)],
          [(0, 0), (1, 0), (1, 1), (2, 1)],
          [(0, 1), (1, 1), (1, 0), (2, 0)],
          [(1, 0), (1, 1), (0, 1), (0, 2)],
          [(0, 0), (0, 1), (1, 1), (1, 2)],
          [(0, 1), (1, 0), (1, 1), (1, 2)],
          [(0, 0), (0, 1), (0, 2), (1, 1)],
          [(0, 0), (1, 0), (1, 1), (2, 0)],
          [(0, 1), (1, 1), (1, 0), (2, 1)]]


def find_max(sr, sc):
    s = 0
    for t in tetris:
        temp = 0
        for dr, dc in t:
            nr, nc = dr + sr, dc + sc
            if 0 <= nr < n and 0 <= nc < m:
                temp += graph[nr][nc]
            else:
                temp = 0
                break
        if temp != 0:
            s = max(temp, s)

    return s


answer = 0
for r in range(n):
    for c in range(m):
        temp = find_max(r, c)
        answer = max(answer, temp)

print(answer)
