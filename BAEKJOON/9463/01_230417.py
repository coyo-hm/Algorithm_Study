import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
  n = int(input())
  sticker = [list(map(int, input().split())) for _ in range(2)]
  for i in range(1, n):
    for j in range(2):
      if i < 2:
        sticker[j][i] += sticker[j - 1][i - 1]
      else:
        sticker[j][i] += max(sticker[j - 1][i - 1], sticker[j][i-2], sticker[j - 1][i-2])

  print(max(sticker[0][n - 1], sticker[1][n - 1]))