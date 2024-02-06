# https://www.acmicpc.net/problem/16234
# 1:24:09

import sys
import collections

input = sys.stdin.readline

n, l, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

day = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def process(sx, sy):
  united = []
  united.append((sx, sy))
  visited[sx][sy] = True
  summ = data[sx][sy]
  cnt = 1
  
  q = collections.deque()
  q.append((sx, sy))
  
  while q:
    x, y = q.popleft()
    for d in range(4):
      nx = dx[d] + x
      ny = dy[d] + y
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
        if l <= abs(data[x][y] - data[nx][ny]) <= r:
          q.append((nx, ny))
          united.append((nx, ny))
          visited[nx][ny] = True
          summ += data[nx][ny]
          cnt += 1

  if cnt == 1:
    return
  for x, y in united:
    data[x][y] = summ // cnt
  return
    
while True:
  visited = [[False] * n for _ in range(n)]
  flag = 0
  for x in range(n):
    for y in range(n):
      if visited[x][y] == False:
        process(x, y)
        flag += 1
  if flag == n * n:
    break
  day += 1   
        
print(day)

