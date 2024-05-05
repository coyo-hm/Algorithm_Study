# https://www.acmicpc.net/problem/2644

import collections

N = int(input())
P1, P2 = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N + 1)]
v = [0] * (N + 1)

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(start):
  q = collections.deque([start])
  while q:
    node = q.popleft()
    for i in graph[node]:
      if v[i] == 0:
        v[i] = v[node] + 1
        q.append(i)
  
bfs(P1)
print(v[P2] if v[P2] > 0 else -1)