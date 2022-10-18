s = input()

result = 0

for i in s:
  n = int(i)
  result = max(result + n, result * n)

print(result)  