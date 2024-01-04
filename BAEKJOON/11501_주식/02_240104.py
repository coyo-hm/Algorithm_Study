# https://www.acmicpc.net/problem/11501
# 00:45:39

import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    chart = list(map(int, input().split()))
    max_price = deque(sorted([(chart[i], i) for i in range(N)], reverse=True))
    profit = 0
    mp = max_price.popleft()
    for i in range(N):
        price = chart[i]
        if price < mp[0]:
            profit += mp[0] - price
        while max_price and mp[1] <= i:
            mp = max_price.popleft()

    print(profit)
