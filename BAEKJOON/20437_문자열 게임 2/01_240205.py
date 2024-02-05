# https://www.acmicpc.net/problem/20437
# 1:01:07

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    w = list(input().rstrip())
    k = int(input())
    w_dict = {}

    for i, l in enumerate(w):
        w_dict[l] = w_dict.get(l, []) + [i]

    target_letter = [key for key in w_dict if len(w_dict[key]) >= k]

    if len(target_letter) == 0:
        print(-1)
        continue

    short = len(w)
    long = -1

    for l in target_letter:
        arr_idx = w_dict[l]
        for i in range(len(arr_idx) + 1 - k):
            length = arr_idx[i + k - 1] - arr_idx[i] + 1
            short = min(short, length)
            long = max(long, length)

    print(short, long)
