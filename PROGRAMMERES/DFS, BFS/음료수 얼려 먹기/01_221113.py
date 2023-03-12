n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
cnt = 0
visited = [[False] * m for _ in range(n)]

def dfs(graph, visited, x, y):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  visited[x][y] = True
  for d in range(4):
    nx = dx[d] + x
    ny = dy[d] + y
    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
      dfs(graph, visited, nx, ny)

for x in range(n):
  for y in range(m):
    if graph[x][y] == 0 and visited[x][y] == False:
      dfs(graph, visited, x, y)
      cnt += 1

print(cnt)