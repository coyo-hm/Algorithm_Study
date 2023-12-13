# https://www.acmicpc.net/problem/1515
# 3:12:07
import sys

input = sys.stdin.readline
nums = input().rstrip()

N = 0
nums_idx = 0
nums_length = len(nums)
while nums_idx < nums_length:
    N = N + 1
    s = str(N)
    prev = nums_idx
    idx = 0
    for i in range(nums_idx, nums_length):
        if nums[i] in s:
            prev = prev + 1
            idx = s.index(nums[i]) + 1
            s = s[idx:]
        else:
            break
    nums_idx = prev
print(N)
