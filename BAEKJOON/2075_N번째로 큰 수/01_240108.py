# https://www.acmicpc.net/problem/2075
# 00:23:29

import sys

input = sys.stdin.readline

N = int(input())
nums = []

for _ in range(N):
    row = list(map(int, input().split()))
    nums += row
    nums = sorted(nums, reverse=True)[:N]

print(nums[-1])
