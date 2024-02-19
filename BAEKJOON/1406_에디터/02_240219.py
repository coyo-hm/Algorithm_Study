# https://www.acmicpc.net/problem/1406
# 00:08:25

import sys
from collections import deque

input = sys.stdin.readline
left = deque(list(input().rstrip()))
right = deque([])
m = int(input())

for _ in range(m):
    command = input().split()
    if command[0] == "L" and len(left) != 0:
        w = left.pop()
        right.appendleft(w)
    elif command[0] == "D" and len(right) != 0:
        w = right.popleft()
        left.append(w)
    elif command[0] == "B" and len(left) != 0:
        left.pop()
    elif command[0] == "P":
        w = command[1]
        left.append(w)

print("".join(left + right))