import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  graph[i][i] = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1

for k in range(1, n + 1):
  for x in range(1, n + 1):
    for y in range(1, n + 1):
      graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

ans = 0
for i in range(1, n + 1):
  cnt = 0
  for j in range(1, n + 1):
    if 0 < graph[i][j] < INF or 0 < graph[j][i] < INF:
      cnt += 1
  if cnt == n - 1:
    ans += 1
    
print(ans)