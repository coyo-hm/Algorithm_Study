import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
maxRes = -int(1e9)
minRes = int(1e9)

def calc(t, step, a, s, m, d):
    global maxRes, minRes
    if step >= n:
        maxRes = max(maxRes, t)
        minRes = min(minRes, t)
        return

    num = arr[step]

    if a > 0:
        calc(t + num, step + 1, a - 1, s, m, d)
    if s > 0:
        calc(t - num, step + 1, a, s - 1, m, d)
    if m > 0:
        calc(t * num, step + 1, a, s, m - 1, d)
    if d > 0:
        calc(int(t / num), step + 1, a, s, m, d - 1)


calc(arr[0], 1, add, sub, mul, div)

print(maxRes)
print(minRes)