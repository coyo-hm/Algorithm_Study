S = list(input())
result = []
num = 0
for i in S:
  if "0" <= i <= "9":
    num += int(i)
  else:
    result.append(i)
result.sort()
print("".join(result) + str(num))