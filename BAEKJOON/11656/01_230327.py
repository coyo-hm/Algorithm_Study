import sys

input = sys.stdin.readline

s = input().strip()
dic = [s[i:] for i in range(len(s))]
dic.sort()
for d in dic:
  print(d)