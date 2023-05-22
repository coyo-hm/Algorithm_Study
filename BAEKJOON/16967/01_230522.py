import sys

input = sys.stdin.readline
h, w, x, y = map(int, input().split())
b = []
a = [[-1001] * w for _ in range(h)]

for _ in range(h + x):
    b.append(list(map(int, input().split())))

for i in range(h + x):
    for j in range(w + y):
        if (i >= h and j < y) or (i < x and j >= w):
            continue
        if x <= i < h and y <= j < w:
            if a[i][j] != -1001:
                a[i - x][j - y] = b[i][j] - a[i][j]
            elif a[i - x][j - y] != -1001:
                a[i][j] = b[i][j] - a[i - x][j - y]

        elif i < h and j < w:
            a[i][j] = b[i][j]
        elif i >= h or j >= w:
            a[i - x][j - y] = b[i][j]

for i in range(h):
    for j in range(w):
        print(a[i][j], end=" ")
    print()