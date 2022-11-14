import sys
from collections import deque

input = sys.stdin.readline

# 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다.
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)
distance[x] = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

queue = deque([x])
while queue:
  v = queue.popleft()
  for i in graph[v]:
    if distance[i] == -1:
      distance[i] = 1 + distance[v]
      queue.append(i)

flag = True

for i in range(1, n + 1):
  if distance[i] == k:
    print(i)
    flag = False

if flag: print(-1)
