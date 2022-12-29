import sys

input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
  parent[i] = i

for i in range(n):
  data = list(map(int, input().split()))
  for j in range(i + 1, n):
    if data[j] == 1 and find_parent(parent, i + 1) != find_parent(parent, j + 1):
      union_parent(parent, i + 1, j + 1)

data = list(map(int, input().split()))
root = find_parent(parent, data[0])
flag = "YES"

for i in data[1:]:
  if root != find_parent(parent, i):
    flag = "NO"
    break
  
print(flag)