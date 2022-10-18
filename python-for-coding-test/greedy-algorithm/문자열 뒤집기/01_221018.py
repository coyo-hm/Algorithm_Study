S = input()

zeroCnt = 0
oneCnt = 0

for i in range(1, len(S)):
  if S[i] != S[i - 1]:
    if S[i - 1] == "0":
      zeroCnt += 1
    else:
      oneCnt += 1
    if i == len(S) - 1:
      if S[i] == "0":
        zeroCnt += 1
      else:
        oneCnt += 1

print(min(oneCnt, zeroCnt))