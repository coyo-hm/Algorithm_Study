import sys
import collections
input = sys.stdin.readline
n = int(input())
ls = list(map(int, input().split()))
ls.sort()
ls = collections.deque(ls)
cnt = 0

while True:
    g = ls.popleft()
    l = len(ls)
    if g == 1:
        a = ls.pop()
        b = ls.pop()
        ls.append(a + b + g)
        cnt += 1
    elif l > g:
        cnt += g
        a = g
        for i in range(g + 1):
            a += ls.pop()
        ls.append(a)
    else:
        cnt += l
        break

print(cnt)
