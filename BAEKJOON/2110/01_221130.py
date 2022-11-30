import sys
input = sys.stdin.readline

n, c = map(int, input().split())
home = []

for _ in range(n):
  home.append(int(input()))

home.sort()

start = 1
end = home[-1] - home[0]
res = 0

while start <= end:
  mid = (start + end) // 2
  value = home[0]
  cnt = 1

  for i in range(1, n):
    if home[i] >= value + mid:
      value = home[i]
      cnt += 1

  if cnt >= c:
    start = mid + 1
    res = mid
  else:
    end = mid - 1
    
print(res)