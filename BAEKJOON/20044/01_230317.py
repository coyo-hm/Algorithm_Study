import sys
input = sys.stdin.readline
n = int(input())
std = list(map(int, input().split()))
std.sort()
answer = []
for i in range(n):
  answer.append(std[i] + std[2 * n - i - 1])
print(min(answer))