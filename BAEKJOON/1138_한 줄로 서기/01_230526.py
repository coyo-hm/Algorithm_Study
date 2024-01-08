import sys

input = sys.stdin.readline
n = int(input())
heights = list(map(int, input().split()))
arr = []

for i in range(n, 0, -1):
    arr.insert(heights[i - 1], i)

for i in arr:
    print(i, end=" ")