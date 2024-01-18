# https://www.acmicpc.net/problem/2531
# 00:12:51

import sys

input = sys.stdin.readline
N, d, k, c = map(int, input().split())
belts = [int(input()) for _ in range(N)]
belts += belts
cnt = 0

for i in range(N):
    eat = belts[i:i + k]
    eat_cnt = len(set(eat))

    if c not in eat:
        eat_cnt += 1

    if eat_cnt > cnt:
        cnt = eat_cnt

print(cnt)
