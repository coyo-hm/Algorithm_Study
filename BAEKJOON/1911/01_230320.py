import sys
import math

input = sys.stdin.readline

n, l = map(int, input().split())
pool = [list(map(int, input().split())) for _ in range(n)]
pool.sort()
ans = 0
start, end = pool[0]
length = 0
for s, e in pool:
  if s > end:
    ans += length // l
    start = s
    end = s + math.ceil((e - s) / l) * l
    length = math.ceil((e - s) / l) * l
  elif e >= end:
    length = math.ceil((e - start) / l) * l
    end = start + length

if(length != 0):
  ans += length // l

print(ans)