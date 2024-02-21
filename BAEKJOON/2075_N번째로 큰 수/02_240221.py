# https://www.acmicpc.net/problem/2075
# 00:03:53

import sys

input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph = sorted(graph + row, reverse=True)[:n]

print(graph[-1])