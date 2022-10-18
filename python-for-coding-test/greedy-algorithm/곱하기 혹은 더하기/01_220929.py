s = input()

result = 0

for i in s:
  n = int(i)
  if result + n > result * n:
    result += n
  else:
    result *= n

print(result)  