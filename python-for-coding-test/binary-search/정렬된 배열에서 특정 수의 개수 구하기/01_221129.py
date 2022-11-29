import sys
from bisect import bisect_right, bisect_left

input = sys.stdin.readline

n, x = map(int, input().split())
nums = list(map(int, input().split()))

start = bisect_left(nums, x)
end = bisect_right(nums, x)

print(end - start if end - start > 0 else -1)  