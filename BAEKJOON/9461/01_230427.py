import sys

input = sys.stdin.readline
t = int(input())
p = [1] * 101

for i in range(4, 101):
    p[i] = p[i - 2] + p[i - 3]

for _ in range(t):
    n = int(input())
    print(p[n])
