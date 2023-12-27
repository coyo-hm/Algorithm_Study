# https://www.acmicpc.net/problem/19637
# 00:27:16

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
titles = []

for _ in range(N):
    title, limit = input().split()
    titles.append((title, int(limit)))

for _ in range(M):
    score = int(input())
    s, e = 0, N

    while s <= e:
        m = (s + e) // 2
        if titles[m][1] < score:
            s = m + 1
        else:
            e = m - 1

    print(titles[s][0])
