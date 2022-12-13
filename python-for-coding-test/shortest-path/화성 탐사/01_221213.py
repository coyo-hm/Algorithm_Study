import sys
import heapq
input = sys.stdin.readline

t = int(input())

INF = int(1e9)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(t):
  n = int(input())
  graph = []
  distance = [[INF] * n for _ in range(n)]
  

  for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

  q = []
  heapq.heappush(q, (graph[0][0], 0, 0))

  while q:
    dist, x, y = heapq.heappop(q)
    if dist > distance[x][y]:
      continue
    for d in range(4):
      nx = dx[d] + x
      ny = dy[d] + y

      if 0 > nx or nx >= n or ny < 0 or ny >= n:
        continue
      cost = dist + graph[nx][ny]
      heapq.heappush(q, (cost, nx, ny))
      if cost < distance[nx][ny]:
        distance[nx][ny] = cost
  print(distance[n-1][n-1])
  
  