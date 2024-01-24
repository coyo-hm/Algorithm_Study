# https://www.acmicpc.net/problem/20920
# 00:14:05

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
max_cnt = 0
words_cnt = {}

for _ in range(N):
    w = input().rstrip()
    if len(w) >= M:
        words_cnt[w] = words_cnt.get(w, 0) + 1
        max_cnt = max(max_cnt, words_cnt[w])

cnt = [[] for _ in range(max_cnt + 1)]
for w in words_cnt.keys():
    cnt[words_cnt[w]].append(w)
words = []
for i in range(max_cnt, -1, -1):
    temp = sorted(cnt[i], key=lambda x: (-len(x), x))
    words.extend(temp)

for w in words:
    print(w)
