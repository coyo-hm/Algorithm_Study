n = int(input())
a = list(map(int, input().split()))
d = [0] * 24
for i in range(n):
    d[a[i]] += 1
for i in range(1, 24):
    print(d[i], end=' ')
