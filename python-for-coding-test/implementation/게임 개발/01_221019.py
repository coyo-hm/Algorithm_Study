N, M = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

graph[x][y] = 1
cnt = 1
turn = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
  d = (d + 3) % 4
  nx, ny = dx[d] + x, dy[d] + y
  if graph[nx][ny] == 0:
    graph[nx][ny] = 1
    x, y = nx, ny
    cnt += 1
    turn = 0
    continue
  else:
    turn += 1
  if turn == 4:
    nx = x - dx[d]
    ny = y - dy[d]
    if graph[nx][ny] == 0:
        x, y = nx, ny
        cnt += 1
        graph[nx][ny] = 1
    else:
      break
    turn = 0

print(cnt)