import sys

input = sys.stdin.readline
road = int(input())
ml, mk = map(int, input().split())
c = int(input())
bomb = [0] * (road + 1)
ans = "YES"

for i in range(1, 1 + road):
  z = int(input())
  if bomb[i - 1] - bomb[max(0, i - ml)]  + mk < z:
    if c > 0:
      c -= 1
      bomb[i] = bomb[i - 1]
    else:
      ans = "NO"
      break
  else:
    bomb[i] = bomb[i - 1] + mk

print(ans)