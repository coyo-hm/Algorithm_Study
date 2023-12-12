# https://www.acmicpc.net/problem/21921
# 00:15:02

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

max_visitors = sum(visitors[:X])
curr = max_visitors
cnt = 1

for i in range(X, N):
    curr = curr + visitors[i] - visitors[i - X]
    if curr > max_visitors:
        max_visitors = curr
        cnt = 1
    elif curr == max_visitors:
        cnt += 1

if max_visitors == 0:
    print("SAD")
else:
    print(max_visitors)
    print(cnt)
