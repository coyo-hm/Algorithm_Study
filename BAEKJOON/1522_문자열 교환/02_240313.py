# https://www.acmicpc.net/problem/1522
# 00:04:15

import sys

input = sys.stdin.readline

s = list(input().rstrip())
w = s.count("a")
n = len(s)
s = s + s[:w]
answer = int(1e9)

for i in range(n):
    cnt = s[i:i + w].count("b")
    answer = min(answer, cnt)

print(answer)
