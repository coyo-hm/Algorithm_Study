import sys

input = sys.stdin.readline
a, b = map(int, input().split())
primes = [True for _ in range(100001)]
primes[0] = False
primes[1] = False

for i in range(2, int(100000 ** 0.5) + 1):
    if primes[i]:
        for j in range(i, 100001):
            if i * j > 100000:
                break
            primes[i * j] = False
    if i * (i + 1) > 100000:
        break

div = [1 if primes[i] else 0 for i in range(b + 1)]

for i in range(2, b + 1):
    for j in range(2, b + 1):
        if i * j > b:
            break
        if primes[j]:
            div[i * j] = div[i] + 1

ans = 0

for i in range(a, b + 1):
    if primes[div[i]]:
        ans += 1

print(ans)