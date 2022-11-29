import sys
from bisect import bisect_right, bisect_left

input = sys.stdin.readline

n = int(input())
allPart = list(map(int, input().split()))
m = int(input())
order = list(map(int, input().split()))
allPart.sort()

def findPart(x):
  start, end = 0, n
  mid = 0
  while start <= end:
    mid = (start + end) // 2
    if allPart[mid] == x:
      return mid
    if x < allPart[mid]:
      end = mid - 1
    elif x > allPart[mid]:
      start = mid + 1
  return -1

for i in order:
  res = findPart(i)
  print("yes" if res > 0 else "no", end = " ")