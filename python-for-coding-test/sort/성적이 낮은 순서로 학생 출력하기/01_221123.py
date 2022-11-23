n = int(input())
std = []
for i in range(n):
  name, score = input().split()
  std.append((int(score), name))
std.sort()
for score, name in std:
  print(name, end=" ")