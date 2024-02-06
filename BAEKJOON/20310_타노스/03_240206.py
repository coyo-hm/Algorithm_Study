# https://www.acmicpc.net/problem/20310
# 00:17:36

import sys
from collections import Counter, deque

input = sys.stdin.readline
s = deque(list(input().rstrip()))
s_cnt = Counter(s)
zero_cnt = s_cnt.get("0", 0) // 2
one_cnt = s_cnt.get("1", 0) // 2

new_s = deque([])
while one_cnt > 0 and s:
    l = s.popleft()
    if l == "1":
        one_cnt -= 1
    else:
        new_s.append(l)
s = new_s + s
new_s = deque([])
while zero_cnt > 0 and s:
    l = s.pop()
    if l == "0":
        zero_cnt -= 1
    else:
        new_s.appendleft(l)

print("".join(s + new_s))
