import sys
import itertools

input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
p, s, m, d = map(int, input().split())

arr = list("p"*p+"s"*s+"m"*m+"d"*d)
ans = []

MIN = 10**8
MAX = -10**8

def cal(n1, n2, a):
  if a == "p":
    return n1 + n2
  elif a == "s":
    return n1 - n2
  elif a == "m":
    return n1 * n2
  else:
    if n1 < 0 and n2 > 0:
      return abs(n1) // n2 * (-1)
    else: 
      return n1 // n2

for a in itertools.permutations(arr, n - 1):
  res = A[0]
  for i in range(n - 1):
    res = cal(res, A[i + 1], a[i])
  MAX = res if MAX < res else MAX
  MIN = res if MIN > res else MIN

print(MAX)
print(MIN)