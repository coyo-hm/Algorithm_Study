# https://www.acmicpc.net/problem/2607
# 00:11:38

import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
word = list(input().rstrip())
word_dict = Counter(word)
answer = 0

for _ in range(n - 1):
    w = list(input().rstrip())
    w_dict = Counter(w)
    m, p = 0, 0
    for l in set(word + w):
        word_cnt = word_dict.get(l, 0)
        w_cnt = w_dict.get(l, 0)
        if word_cnt > w_cnt:
            m += word_cnt - w_cnt
        else:
            p += w_cnt - word_cnt
    if m < 2 and p < 2:
        answer += 1

print(answer)