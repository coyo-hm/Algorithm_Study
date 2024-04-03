# https://www.acmicpc.net/problem/2493
# 00:10:56

import sys

input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))
receiver = [0] * n

stack = []
for i in range(n):
    while stack:
        if stack[-1][1] > tops[i]:
            receiver[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, tops[i]])


print(*receiver)