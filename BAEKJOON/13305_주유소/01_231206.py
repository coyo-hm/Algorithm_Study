# https://www.acmicpc.net/problem/13305

import sys

input = sys.stdin.readline
N = int(input())
road = list(map(int, input().split()))
gas = list(map(int, input().split()))

min_gas = gas[0]
answer = 0

for i, r in enumerate(road):
    answer += r * min_gas
    if gas[i + 1] < min_gas:
        min_gas = gas[i + 1]

print(answer)
