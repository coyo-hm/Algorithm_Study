import sys
import collections

input = sys.stdin.readline
l = int(input())
ml, mk = map(int, input().split())
c = int(input())
bomb = [0] * (l + 1)
flag = "YES"

for i in range(1, l + 1):
  z = int(input())
  hit = bomb[i - 1] - bomb[max(0, i - ml)]
  if hit + mk >= z:
    bomb[i] = bomb[i - 1] + mk
  else:
    if c > 0:
      c -= 1
      bomb[i] = bomb[i - 1]
    else:
      flag = "NO"
      break

print(flag)