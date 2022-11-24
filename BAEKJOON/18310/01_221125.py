import sys
input = sys.stdin.readline

n = int(input())
apart = list(map(int, input().split()))
apart.sort()
i = (n - 1) // 2
print(apart[i])