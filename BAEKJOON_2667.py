import collections

N = int(input())
graph = []
com=[]
v = [[False]*N]*N

for _ in range(N):
  graph.append(list(map(int, list(input()))))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
  c = []
  q = collections.deque([(y, x)])
  while q:
    a, b = q.popleft()
    c.append((a, b))
    for i in range(4):
      ny = a + dy[i]
      nx = b + dx[i]
      if(0 <= ny < N and 0 <= nx < N):
        if(graph[ny][nx] == 1):
          graph[ny][nx] = 0
          q.append((ny, nx))
  return len(c)

for y in range (N):
  for x in range (N):
    if(graph[y][x] == 1): 
      graph[y][x] = 0
      com.append(bfs(y, x))
    
com.sort()
print(len(com))
for i in com:
  print(i)