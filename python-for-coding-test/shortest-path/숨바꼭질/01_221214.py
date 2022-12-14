import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
distance = [INF] * (1 + n)
distance[1] = 0
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

q = []
heapq.heappush(q, (0, 1))

while q:
  dist, idx = heapq.heappop(q)
  if dist > distance[idx]:
    continue
  cost = dist + 1
  for i in graph[idx]:
    heapq.heappush(q, (cost, i))
    if cost < distance[i]:
      distance[i] = cost

m = max([d for d in distance if d < INF])
id = 0
cnt = 0
for i in range(1, n + 1):
  if distance[i] == m:
    cnt += 1
    if id == 0:
      id = i
  
print(id, m, cnt)