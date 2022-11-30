import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

start, end = 0, n
ans = -1

while start <= end:
  mid = (start + end) // 2
  if mid == nums[mid]:
    ans = mid
    break
  if mid > nums[mid]:
    start = mid + 1
  else:
    end = mid - 1
    
print(ans)