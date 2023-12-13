# https://www.acmicpc.net/problem/19941
# 00:20:59

import sys
import copy

input = sys.stdin.readline
N, K = map(int, input().split())
l_hamburger = list(input().rstrip())
r_hamburger = copy.deepcopy(l_hamburger)

l_cnt, r_cnt = 0, 0
for l_idx in range(N):
    r_idx = N - l_idx - 1
    if l_hamburger[l_idx] == "H":
        for i in range(max(0, l_idx - K), min(l_idx + K + 1, N)):
            if l_hamburger[i] == "P":
                l_hamburger[i] = "X"
                l_cnt += 1
                break
    if r_hamburger[r_idx] == "H":
        for i in range(min(r_idx + K, N - 1), max(-1, r_idx - K - 1), -1):
            if r_hamburger[i] == "P":
                r_hamburger[i] = "X"
                r_cnt += 1
                break

print(max(l_cnt, r_cnt))
