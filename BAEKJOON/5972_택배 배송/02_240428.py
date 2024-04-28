# https://www.acmicpc.net/problem/5972
# 00:06:57

import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0

while q:
    dist, prev_idx = heapq.heappop(q)
    if distance[prev_idx] < dist:
        continue
    for next_idx, cost in graph[prev_idx]:
        new_dist = cost + dist
        if new_dist < distance[next_idx]:
            heapq.heappush(q, (new_dist, next_idx))
            distance[next_idx] = new_dist


print(distance[n])