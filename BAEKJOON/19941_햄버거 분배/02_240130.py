# https://www.acmicpc.net/problem/19941
# 00:11:53

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
front = list(input().rstrip())
back = front[::-1]
front_cnt, back_cnt = 0, 0

for i in range(N):
    if front[i] == "H":
        for j in range(max(0, i - K), min(N, i + K + 1)):
            if front[j] == "P":
                front[j] = "X"
                front_cnt += 1
                break
    if back[i] == "H":
        for j in range(max(0, i - K), min(N, i + K + 1)):
            if back[j] == "P":
                back[j] = "X"
                back_cnt += 1
                break

print(max(front_cnt, back_cnt))
