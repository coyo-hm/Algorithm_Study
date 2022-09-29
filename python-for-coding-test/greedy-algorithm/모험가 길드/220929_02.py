N = int(input())
S = sorted(list(map(int, input().split())))

# print(S)
group = 0
cnt = 0
for i in S:
  cnt += 1
  if i <= cnt:
    group += 1
    cnt = 0
    
print(group)
  
  
  