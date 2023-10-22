import sys
input = sys.stdin.readline
h, w, n, m = map(int, input().split())

c = (w + m) // (1 + m)
r = (h + n) // (1 + n)

# print(r, c)
print(r * c)