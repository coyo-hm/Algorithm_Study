N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

maxN = max(numbers)
result = 0

if(numbers.count(maxN) > 1 and numbers[K] != maxN):
  result = maxN * M
  
else:
  secondMax = max(filter(lambda n: n != maxN, numbers))
  result = maxN * (M // (K + 1) * K + M % (K + 1)) + secondMax * (M // (K + 1))

print(result)