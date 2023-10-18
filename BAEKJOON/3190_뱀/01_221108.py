from collections import deque

N = int(input())
K = int(input())
apples = set([tuple(map(int, input().split())) for _ in range(K)])
L = int(input())
change = [input().split() for _ in range(L)]

length = 1
s = deque([(0, 0)])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0
sec = 0
c = change.pop(0)

while True:
  x, y = s[0]
  x += dx[d]
  y += dy[d]
  sec += 1
  
  if (0 <= x < N) and (0 <= y < N) and (x, y) not in s:
    if((x + 1, y + 1) in apples):
      apples.remove((x + 1, y + 1))
      length += 1
    else: 
      s.pop()
    s.appendleft((x, y))
  else:
    break
    
  if(int(c[0]) == sec):
    if c[1] == "D": 
      d = (d + 1) % 4
    else:
      d = (d + 3) % 4
    if len(change) > 0:
      c = change.pop(0)

print(sec)