# https://www.acmicpc.net/problem/13305
# 00:09:49

import sys

input = sys.stdin.readline
N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
answer = 0

for i in range(N - 1):
    answer += min_price * road[i]
    min_price = min(min_price, price[i + 1])

print(answer)
