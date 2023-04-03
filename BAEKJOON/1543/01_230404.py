import sys
input = sys.stdin.readline
doc = input().strip()
word = input().strip()
n = len(word)
cnt = 0


while doc.find(word) >= 0:
  idx = doc.find(word) + n
  doc = doc[idx:]
  cnt += 1

print(cnt)