# https://www.codetree.ai/training-field/search/problems/adjusting-the-temperature-of-the-data-center/description?tags=%2B1-1+technique&page=1&pageSize=20
import sys

MAX_T = 1000000001

input = sys.stdin.readline
N, X, Y, Z = map(int, input().split())
A = []
B = []

for _ in range(N):
    Ai, Bi = map(int, input().split())
    A.append(Ai)
    B.append(Bi)

A.sort()
B.sort()
A.append(MAX_T)
B.append(MAX_T)

i = 0
j = 0
current_work = N * X
answer = N * X

while i < N or j < N:
    if A[i] <= B[j]:
        current_work += Y - X
        i += 1
    else:
        current_work += Z - Y
        j += 1
    if current_work > answer:
        answer = current_work

print(answer)
