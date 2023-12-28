# https://www.acmicpc.net/problem/22233
# 00:20:28

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
keywords = {}
answer = N

for _ in range(N):
    word = input().rstrip()
    keywords[word] = 0

for _ in range(M):
    blog = input().rstrip().split(",")
    for word in blog:
        if word in keywords and keywords[word] == 0:
            answer -= 1
            keywords[word] += 1
    print(answer)
