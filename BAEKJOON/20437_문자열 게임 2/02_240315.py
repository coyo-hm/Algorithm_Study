# https://www.acmicpc.net/problem/20437
# 00:20:30

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w = list(input().rstrip())
    k = int(input())
    letter_dict = {}

    for i, l in enumerate(w):
        letter_dict[l] = letter_dict.get(l, []) + [i]

    target_letter = [l for l in letter_dict if len(letter_dict[l]) >= k]

    if len(target_letter) == 0:
        print(-1)
        continue

    ans_short = len(w)
    ans_long = -1

    for l in target_letter:
        arr = letter_dict[l]
        for i in range(len(arr) + 1 - k):
            length = arr[i + k - 1] - arr[i] + 1
            ans_short = min(ans_short, length)
            ans_long = max(ans_long, length)

    print(ans_short, ans_long)
