# https://www.acmicpc.net/problem/14499
# 00:54:50

import sys

input = sys.stdin.readline

n, m, y, x, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
dice = [0] * 6

for c in commands:
    if c == 1:
        nx = x + 1
        if 0 <= nx < m:
            temp = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[3]
            dice[3] = dice[4]
            dice[4] = temp
            if graph[y][nx] != 0:
                dice[1] = graph[y][nx]
                graph[y][nx] = 0
            else:
                graph[y][nx] = dice[1]
            print(dice[3])
            x = nx
    elif c == 2:
        nx = x - 1
        if 0 <= nx < m:
            temp = dice[1]
            dice[1] = dice[4]
            dice[4] = dice[3]
            dice[3] = dice[5]
            dice[5] = temp
            if graph[y][nx] != 0:
                dice[1] = graph[y][nx]
                graph[y][nx] = 0
            else:
                graph[y][nx] = dice[1]
            print(dice[3])
            x = nx
    elif c == 3:
        ny = y - 1
        if 0 <= ny < n:
            temp = dice[1]
            dice[1] = dice[0]
            dice[0] = dice[3]
            dice[3] = dice[2]
            dice[2] = temp
            if graph[ny][x] != 0:
                dice[1] = graph[ny][x]
                graph[ny][x] = 0
            else:
                graph[ny][x] = dice[1]
            print(dice[3])
            y = ny

    elif c == 4:
        ny = y + 1
        if 0 <= ny < n:
            temp = dice[1]
            dice[1] = dice[2]
            dice[2] = dice[3]
            dice[3] = dice[0]
            dice[0] = temp
            if graph[ny][x] != 0:
                dice[1] = graph[ny][x]
                graph[ny][x] = 0
            else:
                graph[ny][x] = dice[1]
            print(dice[3])
            y = ny
