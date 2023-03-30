import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
  n = int(input())
  up = list(map(int, list(input().strip())))
  down = input().strip()
  ans = 0
  for i in range(n):
    if i == 0:
      if up[0] != 0 and up[1] != 0:
        up[0] -= 1
        up[1] -= 1
        ans += 1
    elif i == n - 1:
      if up[i] != 0 and up[i - 1] != 0:
        up[i] -= 1
        up[i - 1] -= 1
        ans += 1
    else:
      if up[i - 1] != 0 and up[i] != 0 and up[i + 1] != 0:
        up[i] -= 1
        up[i - 1] -= 1
        up[i + 1] -= 1
        ans += 1
  print(ans)