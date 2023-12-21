# https://www.acmicpc.net/problem/20310

import sys

input = sys.stdin.readline
S = input().rstrip()
len_S = len(S)
len_one, len_zero = S.count("1"), S.count("0")
answer = ""
cnt_one, cnt_zero = 0, 0

for s in S:
    if s == "1" and cnt_one < len_one // 2:
        cnt_one += 1
    elif s == "0" and cnt_zero < len_zero // 2:
        answer += s
        cnt_zero += 1
    elif s == "0":
        continue
    else:
        answer += s

print(answer)
