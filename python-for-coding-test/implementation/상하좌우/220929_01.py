N = int(input())
D = input().split()

x, y = 0, 0

for d in D:
  if d == "L":
    if 0 <= y - 1 < N:
      y -= 1
  elif d == "R":
    if 0 <= y + 1 < N:
      y += 1
  elif d == "U":
    if 0 <= x - 1 < N:
      x -= 1
  elif d == "D":
    if 0 <= x + 1 < N:
      x += 1

print(x + 1, y + 1)