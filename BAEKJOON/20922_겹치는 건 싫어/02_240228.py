# https://www.acmicpc.net/problem/20922
# 0:09:07

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
nums = list(map(int, input().split()))
counters = [0] * (max(nums) + 1)

s, e = 0, 0
answer = 0

while e < n:
    if counters[nums[e]] < k:
        counters[nums[e]] += 1
        e += 1
    else:
        counters[nums[s]] -= 1
        s += 1
    answer = max(answer, e - s)

print(answer)
