import sys

input = sys.stdin.readline
t = int(input().strip())

for _ in range(t):
  n = int(input())
  price = list(map(int, input().split()))
  profit = 0
  mp = 0

  for i in range(n - 1, -1, -1):
    if mp < price[i]:
      mp = price[i]
    elif mp > price[i]:
      profit += mp - price[i]

  print(profit)