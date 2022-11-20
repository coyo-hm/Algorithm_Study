import sys
import itertools
input = sys.stdin.readline

n = int(input())
data = []
teacher = []
empty = []

for i in range(n):
  row = input().split()
  data.append(row)
  for j in range(n):
    if row[j] == "T":
      teacher.append((i, j))
    if row[j] == "X":
      empty.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = "NO"

def check():
  for sx, sy in teacher:
    for d in range(4):
      x = sx
      y = sy
      while True:
        nx, ny = x + dx[d], y + dy[d]
        if nx >= n or nx < 0 or ny >= n or ny < 0:
          break
        if data[nx][ny] == "S":
          return False
        if data[nx][ny] == "O":
          break
        x = nx
        y = ny
  return True

for a, b, c in list(itertools.combinations(empty, 3)):
  data[a[0]][a[1]] = "O"
  data[b[0]][b[1]] = "O"
  data[c[0]][c[1]] = "O"
  if check():
    ans = "YES"
    break
  data[a[0]][a[1]] = "X"
  data[b[0]][b[1]] = "X"
  data[c[0]][c[1]] = "X"

print(ans)