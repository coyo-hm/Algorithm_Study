# https://www.acmicpc.net/problem/21921
# 00:09:12

import sys

input = sys.stdin.readline
N, X = map(int, input().split())
visitors = list(map(int, input().split()))
answer, cnt = sum(visitors[:X]), 1
curr = sum(visitors[:X])

for i in range(X, N):
    curr = curr - visitors[i - X] + visitors[i]
    if curr > answer:
        answer = curr
        cnt = 1
    elif curr == answer:
        cnt += 1

if answer == 0:
    print("SAD")
else:
    print(answer)
    print(cnt)
