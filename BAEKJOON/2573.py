import collections

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
q = collections.deque([])
year = 0

def bfs(sx, sy):
  q.append((sx, sy))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if (0 <= nx < N and 0 <= ny < M):
        if(graph[nx][ny] != 0 and visited[nx][ny] == False):
          visited[nx][ny] = True
          q.append((nx, ny))
        elif(graph[nx][ny] == 0):
          melt[x][y] = melt[x][y] + 1
          

while True:
  cnt = 0
  visited = [[False for _ in range(M)] for _ in range(N)]
  melt = [[0 for _ in range(M)] for _ in range(N)]
  for i in range(N):
    for j in range(M):
      if(graph[i][j] != 0 and visited[i][j] == False):
        visited[i][j] = True
        cnt = cnt + 1
        bfs(i, j)
        
  if(cnt >= 2): 
    print(year)
    break
  if(cnt == 0): 
    print(0)
    break
  graph = [[max(graph[i][j] - melt[i][j], 0) for j in range(M)] for i in range(N)]
  year = year + 1