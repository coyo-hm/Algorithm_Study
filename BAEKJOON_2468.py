import collections

def bfs(x, y, h):
  q = collections.deque()
  q.append((x, y))
  visited[x][y] = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if(0 <= nx < N and 0 <= ny < N):
        if(graph[nx][ny] >= h and visited[nx][ny] == 0):
          visited[nx][ny] = 1
          q.append((nx, ny))

N = int(input())
graph = []
maxHeight = 0
minHeight = 101
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
  p = list(map(int, input().split()))
  maxHeight = max(p) if max(p) > maxHeight else maxHeight
  minHeight = min(p) if min(p) < minHeight else minHeight
  graph.append(p)

m = 0
for h in range(minHeight, maxHeight + 1):
  visited = [[0] * N for _ in range(N)]
  place = 0
  for i in range(N):
    for j in range(N):
      if graph[i][j] >= h and visited[i][j] == 0:
        bfs(i, j, h)
        place = place + 1
    if(place > m): m = place

print(m)