N = int(input())
S = sorted(list(map(int, input().split())))

# print(S)
group = 0
cnt = 1
for i in S:
#   print(i, cnt, group)
  if i > cnt:
    cnt += 1
  else:
    group += 1
    cnt = 0
print(group)
  
  
  