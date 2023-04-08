import sys

input = sys.stdin.readline
n, m = map(int, input().split())
h_list = list(map(int, input().split()))
ans = 0
s, e = 1, max(h_list)

while s <= e:
  mid = (s + e) // 2
  t = sum([h - mid for h in h_list if h > mid])
  if t == m:
    ans = mid
    break
  elif t >= m:
    ans = mid
    s = mid + 1
  elif t < m:
    e = mid - 1

print(ans)