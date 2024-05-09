# https://www.acmicpc.net/problem/22251
# 00:32:11


import sys

input = sys.stdin.readline
n, k, p, x = map(int, input().split())
arr_x = list(map(int, list(str(x).zfill(k))))
nums = [[0, 4, 3, 3, 4, 3, 2, 3, 1, 2], [4, 0, 5, 3, 2, 5, 6, 1, 5, 4], [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
        [3, 3, 2, 0, 3, 2, 3, 2, 2, 1], [4, 2, 5, 3, 0, 3, 4, 3, 3, 2], [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
        [2, 6, 3, 3, 4, 1, 0, 5, 1, 2], [3, 1, 4, 2, 3, 4, 5, 0, 4, 3], [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
        [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]]
answer = 0

for f in range(1, n + 1):
    if x == f:
        continue
    cnt = 0
    arr_f = list(str(f).zfill(k))
    for i in range(k):
        cnt += nums[arr_x[i]][int(arr_f[i])]
    if cnt <= p:
        answer += 1
print(answer)
