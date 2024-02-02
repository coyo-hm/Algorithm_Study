# https://softeer.ai/practice/6247
# 00:27:10

import sys

input = sys.stdin.readline
n, q = map(int, input().split())
cars = list(map(int, input().split()))
cars.sort()
cars_dict = {car:idx * (n - idx - 1) for idx, car in enumerate(cars)}

for _ in range(q):
    m = int(input())
    answer = 0
    if m in cars_dict:
        answer = cars_dict[m]
    print(answer)
