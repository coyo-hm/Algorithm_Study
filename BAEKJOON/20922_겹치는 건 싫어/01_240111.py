# https://www.acmicpc.net/problem/20922


import sys

input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
nums_dict = {}
answer = 0

for i in range(N):
    n = nums[i]
    nums_dict[n] = nums_dict.get(n, []) + [i]



# print(nums_dict)
#
# for key in nums_dict:
#     if len(nums_dict[key]) > K:
#         start_idx = 0
#         for i in range(len(nums_dict[key]) - K + 1):
#             end_idx = nums_dict[key][i + K] - 1 if i + K < len(nums_dict[key]) else N
#             length = end_idx - start_idx
#             print(key, i, start_idx, end_idx, length, answer)
#             if answer < length:
#                 answer = length
#             start_idx = nums_dict[key][i] + 1
#         length = N - start_idx
#         if answer < length:
#             answer = length

# print(answer)

s, e = 0, N - 1

while s <= e:
    m