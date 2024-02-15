# https://www.acmicpc.net/problem/22233
# 00:08:20

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
memo = {}

for _ in range(n):
    keyword = input().rstrip()
    memo[keyword] = 1

for _ in range(m):
    keywords = input().rstrip().split(",")
    for keyword in keywords:
        if keyword in memo:
            del memo[keyword]
    print(len(memo.keys()))
