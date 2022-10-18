S = input()

result = 0
for n in S:
  result = max(result + int(n), result * int(n))

print(result)