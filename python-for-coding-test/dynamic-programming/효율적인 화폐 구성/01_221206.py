import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = []
d = [10001] * (m + 1)

for _ in range(n):
  array.append(int(input()))

d[0] = 0
for i in range(n):
  for j in range(array[i], m + 1):
    if d[j - array[i] != 10001]:
      d[j] = min(d[j], d[j - array[i]] + 1)
  
print(d[m] if d[m] != 10001 else -1)