import sys

input = sys.stdin.readline

n, s, r = map(int, input().split())
broken = list(map(int, input().split()))
helper = list(map(int, input().split()))

v = [1] * n

for b in broken:
  v[b - 1] -= 1

helper.sort()

for h in helper:
  idx = h - 1
  v[idx] += 1
  if v[idx] >= 2 and idx - 1 >= 0:
    if v[idx - 1] == 0:
      v[idx] -= 1
      v[idx - 1] += 1
  if v[idx] >= 2 and idx + 1 < n:
    if v[idx + 1] == 0:
      v[idx] -= 1
      v[idx + 1] += 1

print(v.count(0))