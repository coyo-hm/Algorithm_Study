import math
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
X = list(map(int, input().split()))

h = X[0]

for i in range(1, M):
    w = X[i] - X[i - 1]
    if w > 2 * h:
        h = math.ceil(w / 2)

if N - X[-1] > h:
    h = N - X[-1]

print(h)