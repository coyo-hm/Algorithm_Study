# https://www.acmicpc.net/problem/12919
# 00:30:12

import sys
from collections import deque

input = sys.stdin.readline
S = input().rstrip()
T = input().rstrip()
s = len(S)
q = deque([T])
flag = False

while q:
    w = q.popleft()
    # print(w, w[0], w[-1])
    if w == S:
        flag = True
        break
    if len(w) <= s:
        continue
    if w[0] == "B":
        q.append(w[::-1][:-1])
    if w[-1] == "A":
        q.append(w[:-1])


print(1 if flag else 0)