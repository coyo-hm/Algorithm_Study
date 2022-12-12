import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = 1e9
graph = [[INF] * (n + 1) for i in range(n + 1)]

for i in range(1, n + 1):
  graph[i][i] = 0

for _ in range(m):
  x, y = map(int, input().split())
  graph[x][y] = 1
  graph[y][x] = 1

f, k = map(int, input().split())


for z in range(1, n + 1):
  for x in range(1, n + 1):
    for y in range(1, n + 1):
      graph[x][y] = min(graph[x][y], graph[x][z] + graph[z][y])

ans = graph[1][k] + graph[k][f]
print(ans if ans < INF else -1)