# https://www.acmicpc.net/problem/2531
# 00:04:58

import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
answer = 0
belts = [int(input()) for _ in range(n)]
belts = belts + belts[:k]

for i in range(n):
    cnt = set([c] + belts[i:i+k])
    answer = max(answer, len(cnt))

print(answer)