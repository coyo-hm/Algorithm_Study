import sys

input = sys.stdin.readline
n, ns, p = map(int, input().split())

if n == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    ans = -1
    rank = 1

    for i in range(1, n):
        if i >= p:
            break
        if scores[i] < ns:
            if ns == scores[i - 1]:
                ans = rank
            else:
                ans = i + 1
            break
        if scores[i - 1] > scores[i]:
            rank = i + 1

    if ans == -1 and n < p:
        print(n + 1 if scores[-1] > ns else rank)
    else:
        print(ans)
