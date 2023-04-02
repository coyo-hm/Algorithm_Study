import sys

input = sys.stdin.readline

n = int(input())
rank = [int(input()) for _ in range(n)]
rank.sort()

ans = 0
for i in range(n):
  ans += abs(rank[i] - i - 1)
print(ans)