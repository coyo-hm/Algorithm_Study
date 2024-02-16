# https://www.acmicpc.net/problem/1927
# 00:04:19

import sys
import heapq

input = sys.stdin.readline
n = int(input())
heap = []
heapq.heapify(heap)

for _ in range(n):
    x = int(input())
    if x == 0:
        min_n = heapq.heappop(heap) if len(heap) > 0 else 0
        print(min_n)
    else:
        heapq.heappush(heap, x)