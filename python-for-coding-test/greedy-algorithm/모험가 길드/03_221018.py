N = int(input())
Fear = list(map(int, input().split()))
Fear.sort()
cnt = 0
group = 0

for i in Fear:
  print(i, cnt, group)
  group += 1
  if group >= i:
    cnt += 1
    group = 0
    
print(cnt)