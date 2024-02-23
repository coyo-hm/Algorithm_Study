# https://www.acmicpc.net/problem/1260
# 00:13:49

import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for i in range(N)]
V -= 1

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    graph[i] = sorted(graph[i])


def dfs(v, visited):
    visited[v] = True
    print(v + 1, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)


visited = [False] * N
dfs(V, visited)
print()

visited = [False] * N
q = deque([])
q.append(V)
visited[V] = True
while q:
    v = q.popleft()
    print(v + 1, end=" ")
    for i in graph[v]:
        if not visited[i]:
            q.append(i)
            visited[i] = True
