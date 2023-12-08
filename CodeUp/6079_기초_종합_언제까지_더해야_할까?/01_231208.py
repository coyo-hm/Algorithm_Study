n = int(input())
s = 0
for i in range(1, n + 1):
    if s >= n:
        print(i - 1)
        break
    s += i