# https://softeer.ai/practice/6246
# 01:06:46

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
dist = []

for _ in range(m):
    r, c = map(int, input().split())
    dist.append([r - 1, c - 1])

answer = []
drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def find_road(points, depth):
    if depth == m:
        answer.append(points)
        return

    if points[-1] == dist[depth]:
        find_road(points, depth + 1)
        return

    for dr, dc in drc:
        nr, nc = dr + points[-1][0], dc + points[-1][1]
        if 0 <= nr < n and 0 <= nc < n and [nr, nc] not in points and table[nr][nc] == 0:
            find_road(points + [[nr, nc]], depth)


find_road([dist[0]], 0)

# print(answer)
print(len(answer))
