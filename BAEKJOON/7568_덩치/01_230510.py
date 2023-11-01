import sys
input = sys.stdin.readline
n = int(input())
weight = []
height = []
rank = [1] * n

for _ in range(n):
    x, y = map(int, input().split())
    weight.append(x)
    height.append(y)

for i in range(n):
    for j in range(i + 1, n):
        if weight[i] < weight[j] and height[i] < height[j]:
            rank[i] += 1
        elif weight[i] > weight[j] and height[i] > height[j]:
            rank[j] += 1

for r in rank:
    print(r, end=" ")