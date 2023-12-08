h, w = map(int, input().split())
n = int(input())
graph = [[0] * (w + 1) for _ in range(h + 1)]

for _ in range(n):
    l, d, y, x = map(int, input().split())
    if d == 0: #가로
        for i in range(x, x + l):
            graph[y][i] = 1
    elif d == 1: #세로
        for i in range(y, y + l):
            graph[i][x] = 1

for r in range(1, h + 1):
    print(" ".join([str(i) for i in graph[r][1:]]))