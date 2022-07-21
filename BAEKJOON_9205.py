import collections

def bfs():
  q = collections.deque([(home[0], home[1])])
  while q:
    x, y = q.popleft()
    if abs(x - des[0]) + abs(y - des[1]) <= 1000:
      print("happy")
      return
    for i in range(n):
      if not visited[i]:
        nx, ny = con[i]
        if abs(x - nx) + abs(y - ny) <= 1000:
          q.append((nx, ny))
          visited[i] = True
  print("sad")
  return

t = int(input())
for _ in range(t):
  n = int(input())
  home = list(map(int, input().split()))
  con = []
  for _ in range(n):
    con.append(list(map(int, input().split())))
  des = list(map(int, input().split()))
  visited = [False for i in range(n + 1)]
  bfs()