# https://www.codetree.ai/training-field/search/problems/adjusting-the-temperature-of-the-data-center/description?tags=%2B1-1+technique&page=1&pageSize=20
import sys

MAX_T = 1000000001

input = sys.stdin.readline
n, c, g, h = map(int, input().split())
A = []
B = []

for _ in range(n):
    ta, tb = map(int, input().split())
    A.append(ta)
    B.append(tb)

A.sort()
B.sort()
A.append(MAX_T)
B.append(MAX_T)

i = 0
j = 0
current_work = n * c
answer = n * c

while i < n or j < n:
    if A[i] <= B[j]:
        current_work += g - c
        i += 1
    else:
        current_work += h - g
        j += 1
    if current_work > answer:
        answer = current_work

print(answer)
