# https://www.acmicpc.net/problem/1406
# 00:25:37

import sys
from collections import deque

input = sys.stdin.readline
left = deque(list(input().rstrip()))
right = deque()
M = int(input())

for _ in range(M):
    command = input().split()
    if command[0] == "L" and left:
        right.appendleft(left.pop())
    elif command[0] == "D" and right:
        left.append(right.popleft())
    elif command[0] == "B" and left:
        left.pop()
    elif command[0] == "P":
        left.append(command[1])

for c in left:
    print(c, end="")
for c in right:
    print(c, end="")
