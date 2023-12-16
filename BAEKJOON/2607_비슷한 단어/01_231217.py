# https://www.acmicpc.net/problem/2607
# 00:44:07

import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
word = list(input().rstrip())
word_dict = Counter(word)
cnt = 0

for _ in range(N - 1):
    w = list(input().rstrip())
    w_dict = Counter(w)
    m, p = 0, 0

    for k in set(word + w):
        a = word_dict.get(k, 0)
        b = w_dict.get(k, 0)
        if a - b > 0:
            m += a - b
        else:
            p += b - a

    if m < 2 and p < 2:
        cnt += 1

print(cnt)
