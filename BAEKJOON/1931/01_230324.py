import sys
import heapq

input = sys.stdin.readline
meeting = []
cnt = 0
preEnd = 0
n = int(input())

for _ in range(n):
  s, e = map(int, input().split())
  heapq.heappush(meeting, (e, s))

while meeting:
  e, s = heapq.heappop(meeting)
  if s >= preEnd:
    preEnd = e
    cnt += 1

print(cnt)