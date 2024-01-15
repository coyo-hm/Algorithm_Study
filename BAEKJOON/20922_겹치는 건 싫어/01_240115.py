# https://www.acmicpc.net/problem/20922
# 2:01:51

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

counters = [0] * (max(nums) + 1)
s, e = 0, 0
answer = 0

while e < N:
    if counters[nums[e]] < K:
        counters[nums[e]] += 1
        e += 1
    else:
        counters[nums[s]] -= 1
        s += 1

    answer = max(answer, e - s)

print(answer)