S = input()

s = []
cnt = 0

for i in S:
  if "A" <= i <= "Z":
    s.append(i)
  else:
    cnt += int(i)

s.sort()
print("".join(s) + str(cnt) if cnt != 0 else "".join(s))