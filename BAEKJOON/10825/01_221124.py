import sys
input = sys.stdin.readline
n = int(input())
stds = []

for _ in range(n):
  name, kor, eng, math = input().split()
  stds.append((name, int(kor), int(eng), int(math)))

stds.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in stds:
  print(s[0])
  