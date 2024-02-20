# https://www.acmicpc.net/problem/2304
# 00:33:28

import sys

input = sys.stdin.readline
n = int(input())
graph = []
answer = 0
max_y = 0

for _ in range(n):
    x, y = map(int, input().split())
    graph.append((x, y))
    if y > max_y:
        max_y = y

graph.sort()
mid = 0
prev_idx = 0

for i in range(n):
    x, y = graph[i]
    if y > graph[prev_idx][1]:
        answer += (x - graph[prev_idx][0]) * graph[prev_idx][1]
        prev_idx = i
    if y == max_y:
        mid = i
        prev_idx = n - 1
        break

for i in range(n - 1, mid - 1, -1):
    x, y = graph[i]
    if y > graph[prev_idx][1]:
        answer += (graph[prev_idx][0] - x) * graph[prev_idx][1]
        prev_idx = i

answer += (graph[prev_idx][0] - graph[mid][0] + 1) * graph[mid][1]

print(answer)