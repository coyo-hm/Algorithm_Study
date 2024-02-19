# https://www.acmicpc.net/problem/11501
# 00:20:39

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    stocks = list(map(int, input().split()))
    max_price = stocks[-1]
    profit = 0

    for i in range(n - 2, -1, -1):
        price = stocks[i]
        if price < max_price:
            profit += (max_price - price)
        elif price > max_price:
            max_price = price

    print(profit)
