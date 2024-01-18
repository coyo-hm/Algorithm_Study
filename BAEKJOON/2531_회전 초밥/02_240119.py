# https://www.acmicpc.net/problem/2531

import sys

input = sys.stdin.readline
N, d, k, c = map(int, input().split())
belts = [int(input()) for _ in range(N)]
belts += belts
cnt = 0

for i in range(N):
    eat = belts[i:i + k] + [c]
    eat_cnt = len(set(eat))
    if eat_cnt > cnt:
        cnt = eat_cnt

print(cnt)
