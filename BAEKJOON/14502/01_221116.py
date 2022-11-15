#0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 
#2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수
#빈 칸의 개수는 3개 이상이다.

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]
res = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x, y):
  for d in range(4):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
      temp[nx][ny] = 2
      virus(nx, ny)

def getScore():
  score = 0
  for r in temp:
    for c in r:
      if c == 0:
        score += 1
  return score

def dfs(cnt):
  global res
  if cnt == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = graph[i][j]
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i, j)
    res = max(getScore(), res)
    return
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        cnt += 1
        dfs(cnt)
        graph[i][j] = 0
        cnt -= 1
        
dfs(0)
print(res)