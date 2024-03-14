# https://www.acmicpc.net/problem/12919
# 00:16:36

import sys
from collections import deque

input = sys.stdin.readline
s = input().rstrip()
t = input().rstrip()
l = len(s)

q = deque([t])
answer = 0

while q:
    curr = q.popleft()
    if curr == s:
        answer = 1
        break
    if len(curr) <= l:
        continue
    if curr[-1] == "A":
        q.append(curr[:-1])
    if curr[0] == "B":
        q.append(curr[1:][::-1])

print(answer)
