import sys
import itertools

input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
routine = list(itertools.permutations(a, n))

def checkPossible(r):
    temp = 0
    for m in r:
        temp += m - k
        if temp < 0:
            return False
    return True

ans = 0
for r in routine:
    if checkPossible(r):
        ans += 1

print(ans)