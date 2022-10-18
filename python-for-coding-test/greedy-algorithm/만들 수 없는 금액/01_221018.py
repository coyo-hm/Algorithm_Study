import itertools

N = int(input())
M = list(map(int, input().split()))

nums = set(M)

for i in range(2, N):
  for j in list(itertools.combinations(M, i)):
    nums.add(sum(j))

    
print(list(set(range(1, sum(M))) - nums)[0])