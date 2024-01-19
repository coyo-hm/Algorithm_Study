# https://www.acmicpc.net/problem/1522
# 01:04:53

import sys

input = sys.stdin.readline
S = list(input().rstrip())
a_cnt = S.count("a")

answer = float("inf")
S_length = len(S)
S += S[:a_cnt]

for i in range(S_length):
    answer = min(answer, S[i:i + a_cnt].count("b"))

print(answer)
