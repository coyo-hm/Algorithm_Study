# https://www.acmicpc.net/problem/1927
# 00:05:56

import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    n = int(input())
    if n == 0:
        m = 0
        if len(heap) > 0:
            m = heapq.heappop(heap)
        print(m)
    else:
        heapq.heappush(heap, n)
