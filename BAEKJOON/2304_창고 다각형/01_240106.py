# https://www.acmicpc.net/problem/2304
# 00:24:14

import sys

input = sys.stdin.readline
N = int(input())
graph = []
max_y, S = 0, 0

for _ in range(N):
    x, y = map(int, input().split())
    graph.append((x, y))
    if y > max_y:
        max_y = y

graph.sort()

curr_y = graph[0][1]
curr_x = graph[0][0]
mid_index = 0

for i in range(N):
    x, y = graph[i]
    if y == max_y:
        S += (x - curr_x) * curr_y
        mid_index = i
        break
    elif y > curr_y:
        S += (x - curr_x) * curr_y
        curr_x = x
        curr_y = y

curr_y = graph[N - 1][1]
curr_x = graph[N - 1][0] + 1

for i in range(N - 1, mid_index - 1, -1):
    x, y = graph[i]
    if y > curr_y:
        S += (curr_x - x - 1) * curr_y
        curr_x = x + 1
        curr_y = y

S += (curr_x - graph[mid_index][0]) * graph[mid_index][1]

print(S)
