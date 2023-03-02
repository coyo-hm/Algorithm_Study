n = int(input())

cnt = 0
coin = [500, 100, 50, 10]

for c in coin:
  cnt += n // c
  n %= c

print(cnt)