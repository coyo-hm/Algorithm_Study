# https://www.acmicpc.net/problem/19637
# 00:12:16

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
titles = []

for _ in range(n):
    title, title_max = input().split()
    titles.append([title, int(title_max)])

answer = []

for _ in range(m):
    power = int(input())
    s, e = 0, n - 1
    while s <= e:
        m = (s + e) // 2
        title, title_max = titles[m]
        if power > title_max:
            s = m + 1
        else:
            e = m - 1
    # print(s, e)
    answer.append(titles[s][0])

for a in answer:
    print(a)