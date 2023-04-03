import sys
input = sys.stdin.readline
k = int(input())
n = 0
cnt = 0


while 2 ** n < k:
  n += 1

while k > 0:
  m = 2 ** (n - cnt)
  if m == k:
    break
  if m <= k:
    k -= m
  cnt += 1


print(2 ** n, cnt)
