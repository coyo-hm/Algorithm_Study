import collections
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph[r][c] = -1
place = 1

while 1:
  cleaned = 0
  for _ in range(4):
    nx = r + dx[(d+3)%4]
    ny = c + dy[(d+3)%4]
    d = (d+3)%4
    if (0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0):
      graph[nx][ny] = -1
      place = place + 1
      r = nx
      c = ny
      cleaned = 1
      break

  if(cleaned == 0):
    if graph[r-dx[d]][c-dy[d]] == 1:
      print(place)
      break
    else: 
      r = r - dx[d]
      c = c - dy[d]