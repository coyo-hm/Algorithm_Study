import sys

input = sys.stdin.readline
t = int(input())

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

for _ in range(t):
    m, n, x, y = map(int, input().split())
    g = lcm(max(m, n), min(m, n))
    res = -1
    for i in range(g // m + 1):
        if (m * i + x - y) % n == 0:
            res = m * i + x
            break
    print(res)