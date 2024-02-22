# https://www.acmicpc.net/problem/1138
# 00:08:12

import sys

input = sys.stdin.readline
n = int(input())
heights = list(map(int, input().split()))
answer = []

for i in range(n - 1, -1, -1):
    answer.insert(heights[i], i + 1)
for v in answer:
    print(v, end=" ")
