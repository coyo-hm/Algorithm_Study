# https://www.acmicpc.net/problem/1260
# 00:15:20

import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)): graph[i].sort()


def dfs(v):
    print(v, end=" ")
    visited[v] = True
    for i in graph[v]:
        if not visited[i]: dfs(i)


def bfs(s):
    q = deque([s])
    visited[s] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


dfs(V)
visited = [False] * (N + 1)
print()
bfs(V)
