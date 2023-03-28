import sys
input = sys.stdin.readline
t = int(input())

def calc(paper):
  while len(paper) > 1:
    temp = ""
    n = len(paper)
    for i in range(n // 2):
      m = i * 2 + 1
      if paper[m - 1] == paper[m + 1]:
        return "NO"
      else:
        temp += paper[m]

    paper = temp
  return "YES"


for _ in range(t):
  paper = list(input().strip())
  ans = calc(paper)
  print(ans)