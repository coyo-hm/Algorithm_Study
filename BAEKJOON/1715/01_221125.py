import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline


n = int(input())
card = [int(input()) for _ in range(n)]
heapify(card)
ans = 0

while len(card) > 1:
  # print(card)
  a = heappop(card)
  b = heappop(card)
  ans += (a + b)
  heappush(card, a + b)
  
print(ans)