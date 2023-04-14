import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = [int(input()) for _ in range(n)]
heapq.heapify(heap)
ans = 0

while len(heap) > 1:
  a = heapq.heappop(heap)
  b = heapq.heappop(heap)
  ans += (a + b)
  heapq.heappush(heap, a + b)

print(ans)