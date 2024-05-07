# https://www.acmicpc.net/problem/1863
# 00:36:46

import sys

input = sys.stdin.readline
n = int(input())
arr = []
answer = 0

for _ in range(n):
    x, y = map(int, input().split())
    while arr and arr[-1] > y:
        arr.pop()
        answer += 1
    if y != 0 and (len(arr) == 0 or arr[-1] < y):
        arr.append(y)

print(answer + len(arr))
