import sys

input = sys.stdin.readline

coin = [500, 100, 50, 10, 5, 1]

n = int(input())
m = 1000 - n
answer = 0
for c in coin:
  answer += m // c
  m = m % c
print(answer)