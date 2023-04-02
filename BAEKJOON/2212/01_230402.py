import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
cor = list(map(int, input().split()))
cor.sort()
gap = []

for i in range(n - 1):
  gap.append(cor[i + 1] - cor[i])

gap.sort()
print(sum(gap[0:n-k]))
