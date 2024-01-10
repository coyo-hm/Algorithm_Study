# https://www.acmicpc.net/problem/1138
# 00:21:10

import sys

input = sys.stdin.readline
N = int(input())
persons = list(map(int, input().split()))
answer = []

for i in range(N - 1, -1, -1):
    answer.insert(persons[i], i + 1)

for p in answer:
    print(p, end=" ")
