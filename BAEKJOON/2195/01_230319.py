import sys
input = sys.stdin.readline

s = input()
p = input().replace("\n","")

cnt = 0
i = 0
j = 1
copy_p = ""

while copy_p != p:
  if p[i:j] in s and j <= len(p):
    j += 1
  else:
    copy_p += p[i:j-1]
    i = j-1
    cnt += 1
print(cnt)