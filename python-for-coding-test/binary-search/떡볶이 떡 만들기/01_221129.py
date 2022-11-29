n, m = map(int, input().split())
riceCake = list(map(int, input().split()))

start, end = 0, max(riceCake)

while start < end:
  h = (start + end) // 2
  s = sum([i - h for i in riceCake if i - h > 0])

  if s < m:
    end = h
  elif s > m:
    start = h
  else:
    break

print(h)  